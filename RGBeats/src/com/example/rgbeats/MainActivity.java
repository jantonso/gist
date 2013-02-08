package com.example.rgbeats;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.provider.MediaStore.MediaColumns;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.content.DialogInterface.OnClickListener;
import android.content.Intent;
import android.content.res.AssetFileDescriptor;
import android.content.res.AssetManager;
import android.database.Cursor;
import android.widget.RelativeLayout;
import android.widget.Toast;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.SoundPool;
import android.media.SoundPool.OnLoadCompleteListener;
import android.widget.ImageView;
import java.util.Random;
/* TODO make dropbox api work
import com.dropbox.client2.DropboxAPI;
import com.dropbox.client2.android.AndroidAuthSession;
import com.dropbox.client2.exception.DropboxException;
import com.dropbox.client2.exception.DropboxUnlinkedException;
import com.dropbox.client2.session.AccessTokenPair;
import com.dropbox.client2.session.AppKeyPair;
import com.dropbox.client2.session.Session;
import com.dropbox.client2.session.Session.AccessType;
*/

public class MainActivity extends Activity {
	/* 
	private DropboxAPI<AndroidAuthSession> dbapi;
	final static private String APP_KEY="86w2vzys3h583yc";
	final static private String APP_SECRET="vionp76nb8nn66l";
	final static private AccessType ACCESS_TYPE = com.dropbox.client2.session.Session.AccessType.APP_FOLDER;
	*/
	
	public char[] colors=new char[3];
	boolean[] picture=new boolean[3];
	public int currp=0;
	public int latestfile=0;
	public String newsongname;
	public boolean newsong=false;
	public AssetFileDescriptor afd;
	public MediaPlayer mp;
	public SoundPool sp;
	public boolean spactive=false;
	public int[] streamids = new int[3];
	public int filenamecounter = 1;
	//public AccessTokenPair tokens;
	//public File sdpath = getExternalStorageDirectory();
	AssetManager am;
	private OnClickListener buttonclickhandler;
	
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        //AppKeyPair appkeys=new AppKeyPair(APP_KEY,APP_SECRET);
        //AndroidAuthSession session=new AndroidAuthSession(appkeys,ACCESS_TYPE);
        //dbapi=new DropboxAPI<AndroidAuthSession>(session); 
        
        am=this.getAssets();
        mp=new MediaPlayer();
        sp=new SoundPool(5,AudioManager.STREAM_MUSIC,0);
        //afd = new AssetFileDescriptor();
        mp.setOnCompletionListener(new MediaPlayer.OnCompletionListener(){
			@Override
			public void onCompletion(MediaPlayer mp){
				//count++;
				//System.out.print(getString(count));
				if(newsong){
					mp.stop();
					mp.reset();
					//mp.release();
					try {
						afd=getAssets().openFd("Sounds/"+newsongname+".mp3");
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					try {
						mp.setDataSource(afd.getFileDescriptor(),afd.getStartOffset(),afd.getLength());
					} catch (IllegalArgumentException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (IllegalStateException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					try {
						mp.prepare();
					} catch (IllegalStateException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
					//mp.start()
					
					newsong=false;
					mp.start();
				}
				else{
					mp.start();
				}
			}
			
		});
        //  colors[0]=colors[1]=colors[2]='\0';
        sp.setOnLoadCompleteListener(new OnLoadCompleteListener(){
        	@Override
			public void onLoadComplete(SoundPool sp, int sampleid, int status){
        		if(status==0){
        			sp.play(sampleid, 1, 1, currp-1, -1, 1);
        		}
        	}
        });
        
        // new josh stuff
        
    	// START HEADER
        
        final ImageView nav_buttons_cameraroll = (ImageView) findViewById(R.id.nav_buttons_cameraroll);
 	    nav_buttons_cameraroll.setClickable(true);
 	    nav_buttons_cameraroll.setOnClickListener(new View.OnClickListener() {
 	        @Override
 	        public void onClick(View view) {
 	        	getPicture(view);
 	       }
 	    });
        
 	   final ImageView nav_buttons_facebook = (ImageView) findViewById(R.id.nav_buttons_facebook);
	    nav_buttons_facebook.setClickable(true);
	    nav_buttons_facebook.setOnClickListener(new View.OnClickListener() {
	        @Override
	        public void onClick(View view) {
	        	//"Do FACEBOOK THING!"
	       }
	    });
	    
	    final ImageView nav_buttons_dropbox = (ImageView) findViewById(R.id.nav_buttons_dropbox);
 	    nav_buttons_dropbox.setClickable(true);
 	    nav_buttons_dropbox.setOnClickListener(new View.OnClickListener() {
 	        @Override
 	        public void onClick(View view) {
 	        	//"Do DROPBOX THING!"
 	       }
 	    });
 	    
 	    // END HEADER
        
 	    // START PLAYS/PAUSES SUCH
        ImageView pictureView = (ImageView) findViewById(R.id.imageView);
        pictureView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
            	if (picture[0] == false){
            		Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
	     	       	int CAMERA_PIC_REQUEST = 1337;
	     	        startActivityForResult(cameraIntent, CAMERA_PIC_REQUEST);
         	    }
            }
        }); 
        
        
        final ImageView play1 = (ImageView) findViewById(R.id.play1);
 	   	play1.setClickable(true);
 	   	play1.setOnClickListener(new View.OnClickListener() {
 	   		@Override
 	   		public void onClick(View view) {
 	   			if (picture[0] == true){
 	   				pauseplay();
 	   				//play1.setImageResource(R.drawable.ic_launcher);
 	   			}
 	   		}
 	   	});
 	   
 	   final ImageView pause1 = (ImageView) findViewById(R.id.pause1);
 	   pause1.setClickable(true);
 	   pause1.setOnClickListener(new View.OnClickListener() {
 	       @Override
 	       public void onClick(View view) {
 	    	   if (picture[0] == true){
 	    		   pauseplay();
 	    		   //pause1.setImageResource(R.drawable.ic_launcher);
 	    	   }
 	       }
 	   });
 	   
 	   final ImageView stop1 = (ImageView) findViewById(R.id.stop1);
 	   stop1.setClickable(true);
 	   stop1.setOnClickListener(new View.OnClickListener() {
 	       @Override
 	       public void onClick(View view) {
 	    	   if (picture[0] == true){
 	    		   killtrack(0,view);
 	    		 //  stop1.setImageResource(R.drawable.ic_launcher);
 	    	   }
 	       }
 	   });
         
        ImageView pictureView1 = (ImageView) findViewById(R.id.imageView1);
        pictureView1.setOnClickListener(new View.OnClickListener() {
     	   @Override
            public void onClick(View view) {
     		   if (picture[0] == true && picture[1] == false){
     			   Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
 	     	       int CAMERA_PIC_REQUEST = 1337;
 	     	       startActivityForResult(cameraIntent, CAMERA_PIC_REQUEST);
          	   }
            }
        }); 
         
        final ImageView play2 = (ImageView) findViewById(R.id.play2);
  	   	play2.setClickable(true);
  	   	play2.setOnClickListener(new View.OnClickListener() {
  		   @Override
  	       public void onClick(View view) {
  			   if (picture[1] == true){
  				   pauseplay();
  				  // play2.setImageResource(R.drawable.ic_launcher);
  	    	   }
  	       }
  	   	});
  	   
  	   final ImageView pause2 = (ImageView) findViewById(R.id.pause2);
  	   pause2.setClickable(true);
  	   pause2.setOnClickListener(new View.OnClickListener() {
  	       @Override
  	       public void onClick(View view) {
  	    	   if (picture[1] == true){
  	    		   pauseplay();
  	    		  // pause2.setImageResource(R.drawable.ic_launcher);
  	    	   }
  	       }
  	   });
  	   
  	   final ImageView stop2 = (ImageView) findViewById(R.id.stop2);
  	   stop2.setClickable(true);
  	   stop2.setOnClickListener(new View.OnClickListener() {
  	       @Override
  	       public void onClick(View view) {
  	    	   if (picture[1] == true){
  	    		   killtrack(1, view);
  	    		  // stop2.setImageResource(R.drawable.ic_launcher);
  	    	   }
  	       }
  	   }); 
         
        ImageView pictureView2 = (ImageView) findViewById(R.id.imageView2);
        pictureView2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
         	   if (picture[0] == true && picture[1] == true && picture[2] == false){
         		   Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
 	     	       int CAMERA_PIC_REQUEST = 1337;
 	     	       startActivityForResult(cameraIntent, CAMERA_PIC_REQUEST);
          	   }
            }
        }); 
     
        final ImageView play3 = (ImageView) findViewById(R.id.play3);
 	   	play3.setClickable(true);
 	   	play3.setOnClickListener(new View.OnClickListener() {
 	       @Override
 	       public void onClick(View view) {
 	    	   if (picture[2] == true){
 	    		   pauseplay();
 	    		   //play3.setImageResource(R.drawable.ic_launcher);
 	    	   }
 	      }
 	   });
 	   
 	   final ImageView pause3 = (ImageView) findViewById(R.id.pause3);
 	   pause3.setClickable(true);
 	   pause3.setOnClickListener(new View.OnClickListener() {
 	       @Override
 	       public void onClick(View view) {
 	    	   if (picture[2] == true){
 	    		   pauseplay();
 	    		   //pause3.setImageResource(R.drawable.ic_launcher);
 	    	   }
 	       }
 	   });
 	   
 	   final ImageView stop3 = (ImageView) findViewById(R.id.stop3);
 	   stop3.setClickable(true);
 	   stop3.setOnClickListener(new View.OnClickListener() {
 	       @Override
 	       public void onClick(View view) {
 	    	   if (picture[2] == true){
 	    		   killtrack(2, view);
 	    		   //stop3.setImageResource(R.drawable.ic_launcher);
 	    	   }
 	       }
 	   });
     }
    
    @Override
    protected void onResume(){
    	super.onResume();
    	
    	mp.start();
    	/* NO DROPBOX
		if (dbapi.getSession().authenticationSuccessful()) {
            try {
                // MANDATORY call to complete auth.
                // Sets the access token on the session
                dbapi.getSession().finishAuthentication();

                tokens = dbapi.getSession().getAccessTokenPair();
                if(!sendFiles(latestfile, newsongname))
                {
                	Toast.makeText(this,"Error uploading to Dropbox, try again later",Toast.LENGTH_LONG).show();	
                }
                // Provide your own storeKeys to persist the access token pair
                // A typical way to store tokens is using SharedPreferences
               // storeKeys(tokens.key, tokens.secret);
            } catch (IllegalStateException e) {
                Log.i("DbAuthLog", "Error authenticating", e);
           }
    	}
    	*/
    }
    
    @Override
    protected void onRestart(){
    	super.onRestart();
    	mp.start();
    }
    
    @Override
    protected void onPause(){
    	super.onPause();
    	//mp.pause();
    }
    
    @Override
    protected void onStop(){
    	super.onStop();
    	//mp.pause();
    }
    
    @Override
    protected void onDestroy(){
    	super.onDestroy();
    	mp.stop();
    	mp.reset();
    	mp.release();
    	sp.release();
    }
    
    public void dropbox(View view)
    {
    	mp.pause();
    	//dbapi.getSession().startAuthentication(MainActivity.this);
    }
    
    /* NO DROPBOX API
    public boolean sendFiles(int highfile, String songPath){
    	FileInputStream inputStream = null;
    	//dropbox shit here.
    	for(int i=0;i<highfile;i++)
    	{
	    	try {
	    		String filepath = "/sdcard/DCIM/Camera/rgbimg"+((Integer)(filenamecounter)).toString()+".jpg";
	    	    File file = new File(filepath);
	    	    inputStream = new FileInputStream(file);
	    	    com.dropbox.client2.DropboxAPI.Entry newEntry = dbapi.putFile(filepath, inputStream, file.length(), null, null);
	    	    Log.i("DbExampleLog", "The uploaded file's rev is: " + newEntry.rev);
	    	} catch (DropboxUnlinkedException e) {
	    	    // User has unlinked, ask them to link again here.
	    	    Log.e("DbExampleLog", "User has unlinked.");
	    	    return false;
	    	} catch (DropboxException e) {
	    	    Log.e("DbExampleLog", "Something went wrong while uploading.");
	    	    return false;
	    	} catch (FileNotFoundException e) {
	    	    Log.e("DbExampleLog", "File not found.");
	    	    return false;
	    	} finally {
	    	    if (inputStream != null) {
	    	        try {
	    	            inputStream.close();
	    	        } catch (IOException e) {return false;}
	    	    }
	    	}
    	}
    	// now the song and share
    	String filepath = "/sdcard/"+new String(colors,0,currp)+".mp3";
    	File file = new File(filepath);
    	try {
			inputStream = new FileInputStream(file);
			com.dropbox.client2.DropboxAPI.Entry newEntry = dbapi.putFile(filepath, inputStream, file.length(), null, null);
			DropboxAPI.DropboxLink link = null; //newEntry.path  
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		} catch (DropboxException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
    	return true;
    }
    */
    
    public void takePicture(View view) {
    	Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
    	int CAMERA_PIC_REQUEST = 1337;
    	startActivityForResult(cameraIntent, CAMERA_PIC_REQUEST);
    }
    
    public void getPicture(View view) {
    	Intent galleryIntent = new Intent(Intent.ACTION_PICK, android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
    	int GALLERY_REQ = 1338;
    	startActivityForResult(galleryIntent, GALLERY_REQ);
    }
    
    public void savePicture(Bitmap bmp){
    	MediaStore.Images.Media.insertImage(getContentResolver(), bmp, "rgbimg"+((Integer)(filenamecounter)).toString()+".jpg", "Taken by RGBeats");
    	
    	// old code didnt save in gallery
		//FileOutputStream out = new FileOutputStream("/sdcard/DCIM/Camera/rgbimg"+((Integer)(filenamecounter)).toString()+".jpg");
		//bmp.compress(Bitmap.CompressFormat.JPEG, 90);			
		//filenamecounter++;
    	
    }
    
    @Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data){
    	
		super.onActivityResult(requestCode, resultCode, data);
		if (currp>2) currp=2; // only pictures allowed, so any time it gets past, set it to the last pic
		int CAMERA_PIC_REQUEST = 1337; int GALLERY_REQ = 1338;
		if (requestCode == CAMERA_PIC_REQUEST) {
			// Take a picture with a ccamera
			Bitmap newPicture = (Bitmap) data.getExtras().get("data"); 
		    int[] pixels = new int[newPicture.getHeight()*newPicture.getWidth()];
            newPicture.getPixels(pixels, 0, newPicture.getWidth(), 0, 0, newPicture.getWidth(), newPicture.getHeight());
            Bitmap resizedBitmap = Bitmap.createScaledBitmap(newPicture, 140, 140, false);
            int red; int blue; int green; int totalRed = 0; int totalGreen = 0; int totalBlue = 0;
            int height = newPicture.getHeight();
            int width = newPicture.getWidth();
			for (int i = 0; i < height*width; i++){
				red = (pixels[i] & 0xFF0000) >> 16;
            	green = (pixels[i] & 0xFF00) >> 8;
            	blue = (pixels[i] & 0xFF);
            	totalRed += red; 
            	totalBlue += blue; 
            	totalGreen += green;
			}
			totalRed = totalRed / (height*width);
			totalBlue = totalBlue / (height*width);
			totalGreen = totalGreen / (height*width);	
		    int difference1 = totalRed - totalGreen;
		    int difference2 = totalRed - totalBlue;
			if ((-20 < difference1 && difference1 < 20) && (-20 < difference2 && difference2 < 20)){
				Random rand = new Random();
				int randomNumber = rand.nextInt(3-0);
				if (randomNumber == 0) {
					colors[currp] = 'R'; 
				} else if (randomNumber == 1){
					colors[currp] = 'G';
				} else {colors[currp] = 'B';}
		    } else if (totalRed >= totalBlue && totalRed >= totalGreen){
                colors[currp] = 'R';  
            } else if (totalGreen >= totalBlue && totalGreen >= totalRed){
            	colors[currp] = 'G';
            } else {
            	colors[currp] = 'B';
            }
			if (picture[0] == false){ // first pic taken
				ImageView pictureView = (ImageView) findViewById(R.id.imageView);
				if (colors[currp] == 'R'){pictureView.setImageResource(R.drawable.rock_rhythm_and_bass);}
				else if (colors[currp] == 'G'){pictureView.setImageResource(R.drawable.electro_rhythm_and_base);}
				else {pictureView.setImageResource(R.drawable.jazz_rhythm_and_bass);}
				RelativeLayout.LayoutParams params11 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				params11.topMargin = 240;
				pictureView.setLayoutParams(params11);
		        
		        ImageView newPicture1 = (ImageView) findViewById(R.id.newPicture1);
		        newPicture1.setImageBitmap(resizedBitmap);
		        RelativeLayout.LayoutParams params12 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				params12.topMargin = 247;
				params12.leftMargin = 23;
				newPicture1.setLayoutParams(params12);
				
				ImageView newPlay1 = (ImageView) findViewById(R.id.play1);
				newPlay1.setImageResource(R.drawable.button__play);
				RelativeLayout.LayoutParams playParam1 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				playParam1.topMargin = 270;
				playParam1.leftMargin = 340;
				newPlay1.setLayoutParams(playParam1);
				
				ImageView newPause1 = (ImageView) findViewById(R.id.pause1);
				newPause1.setImageResource(R.drawable.button__pause);
				RelativeLayout.LayoutParams pauseParam1 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				pauseParam1.topMargin = 270;
				pauseParam1.leftMargin = 375;
				newPause1.setLayoutParams(pauseParam1);
				
				ImageView newStop1 = (ImageView) findViewById(R.id.stop1);
				newStop1.setImageResource(R.drawable.button__stop);
				RelativeLayout.LayoutParams stopParam1 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				stopParam1.topMargin = 270;
				stopParam1.leftMargin = 415;
				newStop1.setLayoutParams(stopParam1);
		        
		        picture[0] = true;
			} else if (picture[1] == false){ // 2nd pic taken
				ImageView pictureView1 = (ImageView) findViewById(R.id.imageView1);
				if (colors[0] == 'R'){pictureView1.setImageResource(R.drawable.rock_accompaniment);}
				else if (colors[0] == 'G'){pictureView1.setImageResource(R.drawable.electro_accompaniment);}
				else {pictureView1.setImageResource(R.drawable.jaxx_accompaniment);}
				RelativeLayout.LayoutParams params21 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				params21.topMargin = 413;
				pictureView1.setLayoutParams(params21);
				
				ImageView newPicture2 = (ImageView) findViewById(R.id.newPicture2);
		        newPicture2.setImageBitmap(resizedBitmap);
		        RelativeLayout.LayoutParams params22 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				params22.topMargin = 427;
				params22.leftMargin = 23;
				newPicture2.setLayoutParams(params22);
				
				ImageView newPlay2 = (ImageView) findViewById(R.id.play2);
				newPlay2.setImageResource(R.drawable.button__play);
				RelativeLayout.LayoutParams playParam2 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				playParam2.topMargin = 443;
				playParam2.leftMargin = 340;
				newPlay2.setLayoutParams(playParam2);
				
				ImageView newPause2 = (ImageView) findViewById(R.id.pause2);
				newPause2.setImageResource(R.drawable.button__pause);
				RelativeLayout.LayoutParams pauseParam2 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				pauseParam2.topMargin = 443;
				pauseParam2.leftMargin = 375;
				newPause2.setLayoutParams(pauseParam2);
				
				ImageView newStop2 = (ImageView) findViewById(R.id.stop2);
				newStop2.setImageResource(R.drawable.button__stop);
				RelativeLayout.LayoutParams stopParam2 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				stopParam2.topMargin = 443;
				stopParam2.leftMargin = 415;
				newStop2.setLayoutParams(stopParam2);
				
		        picture[1] = true;
			} else if (picture[2] == false){ // third pic taken
				ImageView pictureView2 = (ImageView) findViewById(R.id.imageView2);
				if (colors[0] == 'R'){pictureView2.setImageResource(R.drawable.rock_lead);}
				else if (colors[0] == 'G'){pictureView2.setImageResource(R.drawable.electro_lead);}
				else {pictureView2.setImageResource(R.drawable.jazz_lead);}
				RelativeLayout.LayoutParams params31 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				params31.topMargin = 586;
				pictureView2.setLayoutParams(params31);
				
				ImageView newPicture3 = (ImageView) findViewById(R.id.newPicture3);
		        newPicture3.setImageBitmap(resizedBitmap);
		        RelativeLayout.LayoutParams params32 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				params32.topMargin = 608;
				params32.leftMargin = 23;
				newPicture3.setLayoutParams(params32);
				
				ImageView newPlay3 = (ImageView) findViewById(R.id.play3);
				newPlay3.setImageResource(R.drawable.button__play);
				RelativeLayout.LayoutParams playParam3 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				playParam3.topMargin = 616;
				playParam3.leftMargin = 340;
				newPlay3.setLayoutParams(playParam3);
				
				ImageView newPause3 = (ImageView) findViewById(R.id.pause3);
				newPause3.setImageResource(R.drawable.button__pause);
				RelativeLayout.LayoutParams pauseParam3 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				pauseParam3.topMargin = 616;
				pauseParam3.leftMargin = 375;
				newPause3.setLayoutParams(pauseParam3);
				
				ImageView newStop3 = (ImageView) findViewById(R.id.stop3);
				newStop3.setImageResource(R.drawable.button__stop);
				RelativeLayout.LayoutParams stopParam3 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
				stopParam3.topMargin = 616;
				stopParam3.leftMargin = 415;
				newStop3.setLayoutParams(stopParam3);
				
				picture[2] = true;
			}
			currp++;filenamecounter++;
			savePicture(newPicture);
		} else if(requestCode == GALLERY_REQ){
			// use gallery to  get pic
			if(resultCode == RESULT_OK){  
	            Uri selectedImage = data.getData();
	            String[] filePathColumn = {MediaColumns.DATA};

	            Cursor cursor = getContentResolver().query(selectedImage, filePathColumn, null, null, null);
	            cursor.moveToFirst();

	            int columnIndex = cursor.getColumnIndex(filePathColumn[0]);
	            String filePath = cursor.getString(columnIndex);
	            cursor.close();

	            Bitmap newPicture = BitmapFactory.decodeFile(filePath);
	            
			    int[] pixels = new int[newPicture.getHeight()*newPicture.getWidth()];
	            newPicture.getPixels(pixels, 0, newPicture.getWidth(), 0, 0, newPicture.getWidth(), newPicture.getHeight());
	            Bitmap resizedBitmap = Bitmap.createScaledBitmap(newPicture, 140, 140, false);
	            int red; int blue; int green; int totalRed = 0; int totalGreen = 0; int totalBlue = 0;
	            int height = newPicture.getHeight();
	            int width = newPicture.getWidth();
				for (int i = 0; i < height*width; i++){
					red = (pixels[i] & 0xFF0000) >> 16;
	            	green = (pixels[i] & 0xFF00) >> 8;
	            	blue = (pixels[i] & 0xFF);
	            	totalRed += red; 
	            	totalBlue += blue; 
	            	totalGreen += green;
				}
				totalRed = totalRed / (height*width);
				totalBlue = totalBlue / (height*width);
				totalGreen = totalGreen / (height*width);	
			    int difference1 = totalRed - totalGreen;
			    int difference2 = totalRed - totalBlue;
				if ((-20 < difference1 && difference1 < 20) && (-20 < difference2 && difference2 < 20)){
					Random rand = new Random();
					int randomNumber = rand.nextInt(3-0);
					if (randomNumber == 0) {
						colors[currp] = 'R'; 
					} else if (randomNumber == 1){
						colors[currp] = 'G';
					} else {colors[currp] = 'B';}
			    } else if (totalRed >= totalBlue && totalRed >= totalGreen){
	                colors[currp] = 'R';  
	            } else if (totalGreen >= totalBlue && totalGreen >= totalRed){
	            	colors[currp] = 'G';
	            } else {
	            	colors[currp] = 'B';
	            }
				if (picture[0] == false){ // first pic
					ImageView pictureView = (ImageView) findViewById(R.id.imageView);
					if (colors[0] == 'R'){pictureView.setImageResource(R.drawable.rock_rhythm_and_bass);}
					else if (colors[0] == 'G'){pictureView.setImageResource(R.drawable.electro_rhythm_and_base);}
					else {pictureView.setImageResource(R.drawable.jazz_rhythm_and_bass);}
					RelativeLayout.LayoutParams params11 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					params11.topMargin = 240;
					pictureView.setLayoutParams(params11);
			        
			        ImageView newPicture1 = (ImageView) findViewById(R.id.newPicture1);
			        newPicture1.setImageBitmap(resizedBitmap);
			        RelativeLayout.LayoutParams params12 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					params12.topMargin = 247;
					params12.leftMargin = 23;
					newPicture1.setLayoutParams(params12);
					// set play/pause/delete
					ImageView newPlay1 = (ImageView) findViewById(R.id.play1);
					newPlay1.setImageResource(R.drawable.button__play);
					RelativeLayout.LayoutParams playParam1 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					playParam1.topMargin = 270;
					playParam1.leftMargin = 340;
					newPlay1.setLayoutParams(playParam1);
					
					ImageView newPause1 = (ImageView) findViewById(R.id.pause1);
					newPause1.setImageResource(R.drawable.button__pause);
					RelativeLayout.LayoutParams pauseParam1 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					pauseParam1.topMargin = 270;
					pauseParam1.leftMargin = 375;
					newPause1.setLayoutParams(pauseParam1);
					
					ImageView newStop1 = (ImageView) findViewById(R.id.stop1);
					newStop1.setImageResource(R.drawable.button__stop);
					RelativeLayout.LayoutParams stopParam1 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					stopParam1.topMargin = 270;
					stopParam1.leftMargin = 415;
					newStop1.setLayoutParams(stopParam1);
			        
			        picture[0] = true;
				} else if (picture[1] == false){ // 2nd pic
					ImageView pictureView1 = (ImageView) findViewById(R.id.imageView1);
					if (colors[0] == 'R'){pictureView1.setImageResource(R.drawable.rock_accompaniment);}
					else if (colors[0] == 'G'){pictureView1.setImageResource(R.drawable.electro_accompaniment);}
					else {pictureView1.setImageResource(R.drawable.jaxx_accompaniment);}
					RelativeLayout.LayoutParams params21 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					params21.topMargin = 413;
					pictureView1.setLayoutParams(params21);
					
					ImageView newPicture2 = (ImageView) findViewById(R.id.newPicture2);
			        newPicture2.setImageBitmap(resizedBitmap);
			        RelativeLayout.LayoutParams params22 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					params22.topMargin = 427;
					params22.leftMargin = 23;
					newPicture2.setLayoutParams(params22);
					// set play/pause/delete
					ImageView newPlay2 = (ImageView) findViewById(R.id.play2);
					newPlay2.setImageResource(R.drawable.button__play);
					RelativeLayout.LayoutParams playParam2 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					playParam2.topMargin = 443;
					playParam2.leftMargin = 340;
					newPlay2.setLayoutParams(playParam2);
					
					ImageView newPause2 = (ImageView) findViewById(R.id.pause2);
					newPause2.setImageResource(R.drawable.button__pause);
					RelativeLayout.LayoutParams pauseParam2 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					pauseParam2.topMargin = 443;
					pauseParam2.leftMargin = 375;
					newPause2.setLayoutParams(pauseParam2);
					
					ImageView newStop2 = (ImageView) findViewById(R.id.stop2);
					newStop2.setImageResource(R.drawable.button__stop);
					RelativeLayout.LayoutParams stopParam2 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					stopParam2.topMargin = 443;
					stopParam2.leftMargin = 415;
					newStop2.setLayoutParams(stopParam2);
					
			        picture[1] = true;
				} else if (picture[2] == false){ // 3rd pic
					ImageView pictureView2 = (ImageView) findViewById(R.id.imageView2);
					if (colors[0] == 'R'){pictureView2.setImageResource(R.drawable.rock_lead);}
					else if (colors[0] == 'G'){pictureView2.setImageResource(R.drawable.electro_lead);}
					else {pictureView2.setImageResource(R.drawable.jazz_lead);}
					RelativeLayout.LayoutParams params31 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					params31.topMargin = 586;
					pictureView2.setLayoutParams(params31);
					
					ImageView newPicture3 = (ImageView) findViewById(R.id.newPicture3);
			        newPicture3.setImageBitmap(resizedBitmap);
			        RelativeLayout.LayoutParams params32 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					params32.topMargin = 608;
					params32.leftMargin = 23;
					newPicture3.setLayoutParams(params32);
					// set play/pause/delete
					ImageView newPlay3 = (ImageView) findViewById(R.id.play3);
					newPlay3.setImageResource(R.drawable.button__play);
					RelativeLayout.LayoutParams playParam3 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					playParam3.topMargin = 616;
					playParam3.leftMargin = 340;
					newPlay3.setLayoutParams(playParam3);
					
					ImageView newPause3 = (ImageView) findViewById(R.id.pause3);
					newPause3.setImageResource(R.drawable.button__pause);
					RelativeLayout.LayoutParams pauseParam3 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					pauseParam3.topMargin = 616;
					pauseParam3.leftMargin = 375;
					newPause3.setLayoutParams(pauseParam3);
					
					ImageView newStop3 = (ImageView) findViewById(R.id.stop3);
					newStop3.setImageResource(R.drawable.button__stop);
					RelativeLayout.LayoutParams stopParam3 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
					stopParam3.topMargin = 616;
					stopParam3.leftMargin = 415;
					newStop3.setLayoutParams(stopParam3);
					
					picture[2] = true;
				}
				currp++;filenamecounter++;
			}
		}
		playSound();
    }
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
    
    public void playSound() {
    	//Toast.makeText(this, "Button Pressed", Toast.LENGTH_LONG).show();
    	String filename;
    	if (currp<3 && colors[2]>0) filename=new String(colors);
    	else if (currp==2 && colors[1]=='1') filename=new String(colors,0,1);
    	//else if (currp<2 && colors[1]>0) filename=new String(colors,0,2);
    	else filename=new String(colors,0,currp);
    	
    	//Toast.makeText(this,filename+" "+((Integer)(filename.length())).toString() ,Toast.LENGTH_LONG).show();	
    	if (mp.isPlaying())
    	{
    		newsongname=filename;
    		newsong=true;
    	}
    	else
    	{
    		newsongname=filename;
    		try {
				afd=getAssets().openFd("Sounds/"+filename+".mp3");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			try {
				mp.setDataSource(afd.getFileDescriptor(),afd.getStartOffset(),afd.getLength());
				try {
					mp.prepare();
				} catch (IllegalStateException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			} catch (IllegalArgumentException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IllegalStateException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			//mp.start()
			
			newsong=false;
			mp.start();
    	
    	}
    }
   
    public void pauseplay(){
    	if(mp.isPlaying()){
    		mp.pause();
    	}
    	else{
    		mp.start();
    	}
    }
    
    public void stopNotKill(){
    	if(mp.isPlaying()){
    		mp.stop();
			mp.reset();
			try {
				afd=getAssets().openFd("Sounds/"+newsongname+".mp3");
				mp.setDataSource(afd.getFileDescriptor(),afd.getStartOffset(),afd.getLength());
				mp.prepare();
	    		ImageView pictureView;
		        pictureView = (ImageView) findViewById(R.id.newPicture1);
		        pictureView.setImageResource(android.R.color.transparent);
		        ImageView pictureView1;
		        pictureView1 = (ImageView) findViewById(R.id.newPicture2);
		        pictureView1.setImageResource(android.R.color.transparent);
		        ImageView pictureView2;
		        pictureView2 = (ImageView) findViewById(R.id.newPicture3);
		        pictureView2.setImageResource(android.R.color.transparent);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    	}
    	
    }
    
    public void killtrack(int i, View v){
    	assert(0<=i && i<=2);
    	//TODO switch file
    	if(i==0){
    		if (mp.isPlaying()){
	    		try {
	    			mp.stop();
	    			mp.reset();
					afd=getAssets().openFd("Sounds/"+newsongname+".mp3");
					mp.setDataSource(afd.getFileDescriptor(),afd.getStartOffset(),afd.getLength());
					mp.prepare();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
    		}
    		colors=new char[3];
    		currp=0;
    		picture = new  boolean[3];
    		//mp.stop();mp.reset();
    		//DEAL WITH PICTURES TODO
	        
    		// delete the 1st picture
    		ImageView pictureView = (ImageView) findViewById(R.id.imageView);
			pictureView.setImageResource(R.drawable.camera_button);
			RelativeLayout.LayoutParams params11 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
			params11.topMargin = 240;
			pictureView.setLayoutParams(params11);
    		
    		// delete 1st picture play/pause shit
	        ImageView newPlay1 = (ImageView) findViewById(R.id.play1);
			newPlay1.setImageResource(android.R.color.transparent);
			
			
			ImageView newPause1 = (ImageView) findViewById(R.id.pause1);
			newPause1.setImageResource(android.R.color.transparent);
			
			ImageView newStop1 = (ImageView) findViewById(R.id.stop1);
			newStop1.setImageResource(android.R.color.transparent);
	        
			// delete 2nd picture track
			ImageView pictureView1 = (ImageView) findViewById(R.id.imageView1);
	        pictureView1.setImageResource(R.drawable.camera_button);
			RelativeLayout.LayoutParams params21 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
			params21.topMargin = 413;
			pictureView1.setLayoutParams(params21);
			
			
	        // delete 2nd picture play/pause shit
	        ImageView newPlay2 = (ImageView) findViewById(R.id.play2);
			newPlay2.setImageResource(android.R.color.transparent);
			
			
			ImageView newPause2 = (ImageView) findViewById(R.id.pause2);
			newPause2.setImageResource(android.R.color.transparent);
			
			ImageView newStop2 = (ImageView) findViewById(R.id.stop2);
			newStop2.setImageResource(android.R.color.transparent);
			
			//delete 3rd track
			ImageView pictureView2 = (ImageView) findViewById(R.id.imageView2);
			pictureView2.setImageResource(R.drawable.camera_button);
			RelativeLayout.LayoutParams params31 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
			params31.topMargin = 586;
			pictureView2.setLayoutParams(params31);
			
			// delete 3rd picture play/pause shit
			ImageView newPlay3 = (ImageView) findViewById(R.id.play3);
			newPlay3.setImageResource(android.R.color.transparent);
			
			
			ImageView newPause3 = (ImageView) findViewById(R.id.pause3);
			newPause3.setImageResource(android.R.color.transparent);
			
			ImageView newStop3 = (ImageView) findViewById(R.id.stop3);
			newStop3.setImageResource(android.R.color.transparent);
	        
    	}else if(i==1){ // 2nd picutre
    		/*if(colors[i]=='R'){
    			colors[i]='1';
    		}else if(colors[i]=='G'){
    			colors[i]='2';
    		}else if(colors[i]=='B'){
    			colors[i]='3';
    		}*/
    		colors[i]='1';
    		currp=1;
    		picture[1]=false;
    		playSound();
	        ImageView pictureView1 = (ImageView) findViewById(R.id.imageView1);
	        pictureView1.setImageResource(R.drawable.camera_button);
			RelativeLayout.LayoutParams params21 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
			params21.topMargin = 413;
			pictureView1.setLayoutParams(params21);
    		// DEAL WITH PICTURES
			ImageView newPlay2 = (ImageView) findViewById(R.id.play2);
			newPlay2.setImageResource(android.R.color.transparent);
			
			
			ImageView newPause2 = (ImageView) findViewById(R.id.pause2);
			newPause2.setImageResource(android.R.color.transparent);
			
			ImageView newStop2 = (ImageView) findViewById(R.id.stop2);
			newStop2.setImageResource(android.R.color.transparent);
			
    	}else{ // 3rd picture 
    		colors[i]=0;
    		currp=2;
    		picture[2]=false;
    		playSound();
    		ImageView pictureView2 = (ImageView) findViewById(R.id.imageView2);
			pictureView2.setImageResource(R.drawable.camera_button);
			RelativeLayout.LayoutParams params31 = new RelativeLayout.LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT);
			params31.topMargin = 586;
			pictureView2.setLayoutParams(params31);
    		//DEAL WITH PICTURES
			ImageView newPlay3 = (ImageView) findViewById(R.id.play3);
			newPlay3.setImageResource(android.R.color.transparent);
			
			
			ImageView newPause3 = (ImageView) findViewById(R.id.pause3);
			newPause3.setImageResource(android.R.color.transparent);
			
			ImageView newStop3 = (ImageView) findViewById(R.id.stop3);
			newStop3.setImageResource(android.R.color.transparent);
    	}
    }
    //TODO get phone volume
    public void playSoundPool() throws IOException {
    	//AssetManager am=this.getAssets();
        //Toast.makeText(this, "Button Pressed", Toast.LENGTH_LONG).show();
        colors[0]='G';
        String filename=new String(colors,0,currp);
        //Toast.makeText(this,filename+" "+((Integer)(filename.length())).toString() ,Toast.LENGTH_LONG).show();	
        if (spactive){
        	//Toast.makeText(this,filename+" "+((Integer)(filename.length())).toString() ,Toast.LENGTH_LONG).show();
        	streamids[currp-1]=sp.load("./assets/Sounds/"+filename+".mp3", currp-1);
		//	sp.play(streamids[currp-1], (float)1, (float)1, currp-1, -1, 1);
        }
        else{
        	streamids[currp-1]=sp.load("./assets/Sounds/"+filename+".mp3", currp-1);
			//-sp.play(streamids[currp-1], (float)1, (float)1, currp-1, -1, 1);
			spactive=!spactive;
        }
    }
	
    public void playpausepool(){
    	if(spactive){
    		sp.autoPause();
    		spactive=!spactive;
    	}
    	else{
    		sp.autoResume();
    		spactive=!spactive;
    	}
    }
    
    public void killpooltrack(int i){
    	assert(0<=i && i<=2);
    	//TODO switch file
    	if(i==0){
    		colors=new char[3];
    		currp=0;
    		picture = new  boolean[3];
    		mp.stop();mp.reset();
    		//DEAL WITH PICTURES TODO
    	}else if(i==1){
    		if(colors[i]=='R'){
    			colors[i]='1';
    		}else if(colors[i]=='G'){
    			colors[i]='2';
    		}else if(colors[i]=='B'){
    			colors[i]='3';
    		}
    		currp=1;
    		// DEAL WITH PICTURES
    	}else{
    		colors[i]=0;
    		currp=2;
    		//DEAL WITH PICTURES
    	}
    	spactive=!spactive;
    }
    
}

