<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'clearsync';
$app['version'] = '1.1.0';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('clearsync_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('clearsync_app_name');
$app['category'] = lang('base_category_system');
$app['subcategory'] = lang('base_subcategory_settings');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_only'] = TRUE;

$app['core_requires'] = array(
    'clearsync',
);

$app['core_file_manifest'] = array(
    'clearsyncd.php'=> array('target' => '/var/clearos/base/daemon/clearsyncd.php'),
);
