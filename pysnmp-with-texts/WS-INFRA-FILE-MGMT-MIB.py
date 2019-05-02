#
# PySNMP MIB module WS-INFRA-FILE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WS-INFRA-FILE-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, IpAddress, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "Integer32")
DateAndTime, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TruthValue", "TextualConvention")
wsInfra, = mibBuilder.importSymbols("WS-SMI", "wsInfra")
DoActionNow, = mibBuilder.importSymbols("WS-TYPE-MIB", "DoActionNow")
wsInfraFileMgmtModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1))
wsInfraFileMgmtModule.setRevisions(('2006-10-06 11:14', '2006-07-06 11:49', '2006-06-26 18:57', '2006-05-26 14:52', '2006-05-24 10:44', '2005-11-14 15:48', '2005-11-03 10:14', '2005-10-18 16:12', '2005-10-12 14:10', '2005-10-12 13:55', '2005-10-12 11:03', '2005-10-11 17:33', '2005-08-04 10:18', '2005-07-06 11:49', '2005-06-28 11:58', '2005-06-27 14:34', '2005-06-24 12:07', '2005-06-23 13:17', '2005-06-22 10:34', '2005-06-20 11:05', '2005-06-09 15:24', '2005-06-07 18:43', '2005-05-04 16:13', '2005-05-04 10:58',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wsInfraFileMgmtModule.setRevisionsDescriptions(('01a24', '01a23', '01a22', '01a21', '01a20', '01a19', '01a18', '01a17', '01a16', '01a15', '01a14', '01a13', '01a12', '01a11', '01a10', '01a09', '01a08', '01a07', '01a06', '01a05', '01a04', '01a03', '01a02', '01a01',))
if mibBuilder.loadTexts: wsInfraFileMgmtModule.setLastUpdated('200610061114Z')
if mibBuilder.loadTexts: wsInfraFileMgmtModule.setOrganization('Symbol Technologies')
if mibBuilder.loadTexts: wsInfraFileMgmtModule.setContactInfo('Symbol Technologies, Inc. Customer Service Postal: One Symbol Plaza Holtsville, NY 11742-1300 USA Tel: +1. 631.738.6213 E-mail: support@symbol.com Web: http://www.symbol.com/support')
if mibBuilder.loadTexts: wsInfraFileMgmtModule.setDescription('Description.')
class DoActionState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("success", 1), ("failure", 2), ("inProgress", 3))

wsInfraFileMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2))
wsInfraFileMgmtDir = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 1))
wsInfraFileMgmtDirString = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileMgmtDirString.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtDirString.setDescription('current working directory')
wsInfraFIleMgmtDirError = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFIleMgmtDirError.setStatus('current')
if mibBuilder.loadTexts: wsInfraFIleMgmtDirError.setDescription('error of changing the current working directory')
wsInfraFileTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2), )
if mibBuilder.loadTexts: wsInfraFileTable.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileTable.setDescription('local file table')
wsInfraFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1), ).setIndexNames((0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFileIndex"))
if mibBuilder.loadTexts: wsInfraFileEntry.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileEntry.setDescription('local file table entry')
wsInfraFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: wsInfraFileIndex.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileIndex.setDescription('simple index for file table')
wsInfraFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileName.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileName.setDescription('file name')
wsInfraFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("binary", 1), ("text", 2), ("unknown", 3), ("directory", 4), ("symlink", 5), ("emptyFile", 6), ("unReadableFile", 7), ("logFile", 8), ("historyFile", 9), ("configFile", 10), ("licFile", 11), ("certFile", 12), ("coreFile", 13), ("panicFile", 14), ("dumpFile", 15), ("pcapFile", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileType.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileType.setDescription('file type')
wsInfraFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 4), Integer32()).setUnits('byte').setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileSize.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileSize.setDescription('file size')
wsInfraFilePerm = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFilePerm.setStatus('current')
if mibBuilder.loadTexts: wsInfraFilePerm.setDescription('permission of the file')
wsInfraFileCreateDate = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileCreateDate.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileCreateDate.setDescription('file creation date')
wsInfraFileModDate = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileModDate.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileModDate.setDescription('file modification date')
wsInfraFileMgmtImageTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3), )
if mibBuilder.loadTexts: wsInfraFileMgmtImageTable.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageTable.setDescription('Description.')
wsInfraFileMgmtImageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1), ).setIndexNames((0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageIndex"))
if mibBuilder.loadTexts: wsInfraFileMgmtImageEntry.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageEntry.setDescription('Description.')
wsInfraFileMgmtImageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: wsInfraFileMgmtImageIndex.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageIndex.setDescription('simple index of image table')
wsInfraFileMgmtImageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileMgmtImageVersion.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageVersion.setDescription('version of the image')
wsInfraFileMgmtImageUseNow = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileMgmtImageUseNow.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageUseNow.setDescription('indicate if it is used by the system')
wsInfraFileMgmtImageUseOnBoot = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileMgmtImageUseOnBoot.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageUseOnBoot.setDescription('indicate if it is used on the reboot')
wsInfraFileMgmtImageBuildTime = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileMgmtImageBuildTime.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageBuildTime.setDescription('image build time')
wsInfraFileMgmtImageInstallTime = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 3, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileMgmtImageInstallTime.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImageInstallTime.setDescription('image install time')
wsInfraImgUpd = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4))
wsInfraImgUpdFile = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraImgUpdFile.setStatus('current')
if mibBuilder.loadTexts: wsInfraImgUpdFile.setDescription('image update file, The location can be specified as tftp://<hostname or IP>/path/imgfile or ftp://<user>:<passwd>@<hostname or IP>/path/imgfile')
wsInfraImgUpdStart = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("imgUpdate", 1), ("abortUpdate", 2), ("idle", 3), ("removePatch", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraImgUpdStart.setStatus('current')
if mibBuilder.loadTexts: wsInfraImgUpdStart.setDescription('network file transfer start, set this value to 1 means starting imgUpdate, set to 2 means aborting img update. If there is no imgUpdate, the back end will set this value to idle.')
wsInfraImgUpdStatus = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 3), DoActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraImgUpdStatus.setStatus('current')
if mibBuilder.loadTexts: wsInfraImgUpdStatus.setDescription('status of the file transfer, the possible values are success(1), failure(2) and inProgress. We may need to add more failure return codes in the future. ')
wsInfraImgUpdLastFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraImgUpdLastFailedReason.setStatus('current')
if mibBuilder.loadTexts: wsInfraImgUpdLastFailedReason.setDescription('last fileTransfer/imageUpdate failed reason')
wsInfraImgUpdCounter = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraImgUpdCounter.setStatus('current')
if mibBuilder.loadTexts: wsInfraImgUpdCounter.setDescription('it is a gauge counter which will be increased by every file trasfer action')
wsInfraFileManage = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5))
wsInfraFileManageSrc = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileManageSrc.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileManageSrc.setDescription('name of the src file')
wsInfraFileManageDest = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileManageDest.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileManageDest.setDescription('name of the dest file')
wsInfraFileManageStart = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))).clone(namedValues=NamedValues(("copy", 1), ("delete", 2), ("rename", 3), ("rmDir", 4), ("mkDir", 5), ("importKey", 6), ("importCACert", 7), ("importServerCert", 8), ("importTrustPoint", 9), ("exportKey", 10), ("exportCert", 11), ("exportReq", 12), ("exportTrustPoint", 13), ("idle", 14), ("computeSavedCfgChkSum", 15), ("computeRunningCfgChkSum", 16), ("abort", 17), ("expand", 18), ("cgiImport", 19)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileManageStart.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileManageStart.setDescription('local file management start, setting this value to 1 means copy, 2 means delete, 3 means rename, 4 means rmdir, 5 mean mkdir, and when there is no local file management, the back end will set this value to idle. copy/rename, both src and dest need to be specified delete/rmdir/mkdir, only src needs to be specified Files: flash:/path/file nvram:startup-config system:running-config URLs: tftp://<hostname or IP>/path/file ftp://<user>:<passwd>@<hostname or IP>/path/file scp://<user>@<hostname or IP>/path/file ')
wsInfraFileManageStatus = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 4), DoActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileManageStatus.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileManageStatus.setDescription('state of the file manage, success,failure, or inProgress')
wsInfraFileManageLastFailedReason = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileManageLastFailedReason.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileManageLastFailedReason.setDescription('file manage last failed reason.')
wsInfraFileManageCounter = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileManageCounter.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileManageCounter.setDescription('a guage counter which will be increased by the file manager action')
wsInfraFileImgUpdFailOver = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileImgUpdFailOver.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileImgUpdFailOver.setDescription('if there is an error in img reboot, this attribute instucts the system to do failover or not.It is simply a truth value.')
wsInfraCfgManage = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7))
wsInfraCfgManageRunningCfgChangedFlag = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraCfgManageRunningCfgChangedFlag.setStatus('current')
if mibBuilder.loadTexts: wsInfraCfgManageRunningCfgChangedFlag.setDescription('This is a Boolean variable indicating if the Running Config is different from the Saved Config. It indicates that there are pending changes that have not been saved yet, but the switch is functioning with a config that is different from Saved Config. ')
wsInfraCfgManageSavedCfgChecksum = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraCfgManageSavedCfgChecksum.setStatus('current')
if mibBuilder.loadTexts: wsInfraCfgManageSavedCfgChecksum.setDescription('The checksum of the Saved Config text.')
wsInfraCfgManageRunningCfgChecksum = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraCfgManageRunningCfgChecksum.setStatus('current')
if mibBuilder.loadTexts: wsInfraCfgManageRunningCfgChecksum.setDescription('The checksum of the Running Config text.')
wsInfraCfgManageResultantChecksum = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 7, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraCfgManageResultantChecksum.setStatus('current')
if mibBuilder.loadTexts: wsInfraCfgManageResultantChecksum.setDescription('When FileManageStart is set to compute Saved Config or Running Config Checksum, this variable holds the resultant checksum when the computation is done')
wsInfraFileMgmtPatchTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8), )
if mibBuilder.loadTexts: wsInfraFileMgmtPatchTable.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtPatchTable.setDescription('Table of patch names applied to build.')
wsInfraFileMgmtPatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1), ).setIndexNames((0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchIndex"))
if mibBuilder.loadTexts: wsInfraFileMgmtPatchEntry.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtPatchEntry.setDescription('Patch table entry.')
wsInfraFileMgmtPatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: wsInfraFileMgmtPatchIndex.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtPatchIndex.setDescription('Index using same value as wsInfraFileMgmtPatchName.')
wsInfraFileMgmtPatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileMgmtPatchName.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtPatchName.setDescription('Name of patch.')
wsInfraFileMgmtPatchVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 8, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFileMgmtPatchVersion.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtPatchVersion.setDescription('Version of patch in regex format [0-9]*\\.[0-9]*')
wsInfraFSTable = MibTable((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9), )
if mibBuilder.loadTexts: wsInfraFSTable.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSTable.setDescription('Table of file systems')
wsInfraFSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1), ).setIndexNames((0, "WS-INFRA-FILE-MGMT-MIB", "wsInfraFSIndex"))
if mibBuilder.loadTexts: wsInfraFSEntry.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSEntry.setDescription('Description.')
wsInfraFSIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: wsInfraFSIndex.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSIndex.setDescription('Simple index of file system')
wsInfraFSName = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFSName.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSName.setDescription('Name of file system')
wsInfraFSAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFSAvailable.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSAvailable.setDescription('Indicates if file system is available (e.g. if removeable devices are plugged in) or not')
wsInfraFSFormatted = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFSFormatted.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSFormatted.setDescription('Indicates if file system is formatted or not')
wsInfraFSFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 9, 1, 5), DoActionNow()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraFSFormat.setStatus('current')
if mibBuilder.loadTexts: wsInfraFSFormat.setDescription('Command to format the file system.')
wsInfraFileMgmtImportStatus = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notDone", 1), ("inProgress", 2), ("success", 3), ("failure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraFileMgmtImportStatus.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtImportStatus.setDescription('Status of the CGI import operation.')
wsInfraFileMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100))
wsInfraFileMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 1))
wsInfraFileMgmtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 1, 1)).setObjects(("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileName"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileType"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileSize"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileCreateDate"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileModDate"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageSrc"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageDest"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageStatus"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageLastFailedReason"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageCounter"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileIndex"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileImgUpdFailOver"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileManageStart"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFilePerm"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtDirString"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFIleMgmtDirError"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageIndex"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageVersion"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageUseNow"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageUseOnBoot"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageRunningCfgChecksum"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageSavedCfgChecksum"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageRunningCfgChangedFlag"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchVersion"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchName"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtPatchIndex"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSIndex"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSName"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSAvailable"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSFormatted"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFSFormat"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageInstallTime"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImageBuildTime"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdFile"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdStart"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdStatus"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdLastFailedReason"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraImgUpdCounter"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraCfgManageResultantChecksum"), ("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtImportStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfraFileMgmtGroup = wsInfraFileMgmtGroup.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtGroup.setDescription('Description.')
wsInfraFileMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 2))
wsInfraFileMgmtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 388, 14, 1, 2, 1, 100, 2, 1)).setObjects(("WS-INFRA-FILE-MGMT-MIB", "wsInfraFileMgmtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfraFileMgmtMIBCompliance = wsInfraFileMgmtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: wsInfraFileMgmtMIBCompliance.setDescription('Description.')
mibBuilder.exportSymbols("WS-INFRA-FILE-MGMT-MIB", wsInfraFileMgmtPatchName=wsInfraFileMgmtPatchName, wsInfraFileMgmtImageIndex=wsInfraFileMgmtImageIndex, wsInfraFileManageLastFailedReason=wsInfraFileManageLastFailedReason, wsInfraFileMgmtPatchVersion=wsInfraFileMgmtPatchVersion, wsInfraFileMgmtMIBCompliance=wsInfraFileMgmtMIBCompliance, wsInfraImgUpdStatus=wsInfraImgUpdStatus, wsInfraCfgManageRunningCfgChangedFlag=wsInfraCfgManageRunningCfgChangedFlag, wsInfraFSFormatted=wsInfraFSFormatted, wsInfraFileType=wsInfraFileType, PYSNMP_MODULE_ID=wsInfraFileMgmtModule, wsInfraFileMgmtModule=wsInfraFileMgmtModule, wsInfraFileIndex=wsInfraFileIndex, wsInfraFSName=wsInfraFSName, wsInfraFileMgmtMIBCompliances=wsInfraFileMgmtMIBCompliances, wsInfraFileMgmtImageBuildTime=wsInfraFileMgmtImageBuildTime, wsInfraFileModDate=wsInfraFileModDate, wsInfraFileMgmtGroup=wsInfraFileMgmtGroup, wsInfraFileMgmtImageEntry=wsInfraFileMgmtImageEntry, wsInfraFSEntry=wsInfraFSEntry, wsInfraCfgManage=wsInfraCfgManage, wsInfraFileManage=wsInfraFileManage, wsInfraFSAvailable=wsInfraFSAvailable, wsInfraFileEntry=wsInfraFileEntry, wsInfraFileCreateDate=wsInfraFileCreateDate, wsInfraImgUpdCounter=wsInfraImgUpdCounter, wsInfraFileMgmtPatchTable=wsInfraFileMgmtPatchTable, wsInfraFilePerm=wsInfraFilePerm, wsInfraImgUpdFile=wsInfraImgUpdFile, wsInfraFileMgmtImageUseNow=wsInfraFileMgmtImageUseNow, wsInfraFileMgmtImageInstallTime=wsInfraFileMgmtImageInstallTime, wsInfraFileManageStart=wsInfraFileManageStart, wsInfraFileName=wsInfraFileName, wsInfraFileSize=wsInfraFileSize, wsInfraFileMgmtImageUseOnBoot=wsInfraFileMgmtImageUseOnBoot, wsInfraFileMgmt=wsInfraFileMgmt, wsInfraFIleMgmtDirError=wsInfraFIleMgmtDirError, wsInfraCfgManageRunningCfgChecksum=wsInfraCfgManageRunningCfgChecksum, wsInfraFileMgmtMIBConformance=wsInfraFileMgmtMIBConformance, wsInfraImgUpd=wsInfraImgUpd, wsInfraImgUpdLastFailedReason=wsInfraImgUpdLastFailedReason, wsInfraFSTable=wsInfraFSTable, wsInfraFileMgmtPatchEntry=wsInfraFileMgmtPatchEntry, DoActionState=DoActionState, wsInfraImgUpdStart=wsInfraImgUpdStart, wsInfraFileManageSrc=wsInfraFileManageSrc, wsInfraFileManageStatus=wsInfraFileManageStatus, wsInfraFileMgmtDir=wsInfraFileMgmtDir, wsInfraFileMgmtImageTable=wsInfraFileMgmtImageTable, wsInfraCfgManageSavedCfgChecksum=wsInfraCfgManageSavedCfgChecksum, wsInfraCfgManageResultantChecksum=wsInfraCfgManageResultantChecksum, wsInfraFileManageDest=wsInfraFileManageDest, wsInfraFileImgUpdFailOver=wsInfraFileImgUpdFailOver, wsInfraFileMgmtImportStatus=wsInfraFileMgmtImportStatus, wsInfraFileMgmtImageVersion=wsInfraFileMgmtImageVersion, wsInfraFileMgmtPatchIndex=wsInfraFileMgmtPatchIndex, wsInfraFileMgmtMIBGroups=wsInfraFileMgmtMIBGroups, wsInfraFSIndex=wsInfraFSIndex, wsInfraFileMgmtDirString=wsInfraFileMgmtDirString, wsInfraFSFormat=wsInfraFSFormat, wsInfraFileTable=wsInfraFileTable, wsInfraFileManageCounter=wsInfraFileManageCounter)
