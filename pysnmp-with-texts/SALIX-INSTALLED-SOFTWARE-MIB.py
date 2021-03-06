#
# PySNMP MIB module SALIX-INSTALLED-SOFTWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SALIX-INSTALLED-SOFTWARE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hrSWRunEntry, hrSWInstalledEntry, hrSWInstalledIndex = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrSWRunEntry", "hrSWInstalledEntry", "hrSWInstalledIndex")
salixGeneric, = mibBuilder.importSymbols("SALIX-MIB", "salixGeneric")
SalixPlugInUnitType, = mibBuilder.importSymbols("SALIX-PRODUCT-PLUGIN-MIB", "SalixPlugInUnitType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, NotificationType, Integer32, IpAddress, Counter64, MibIdentifier, TimeTicks, iso, ObjectIdentity, ModuleIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "Integer32", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "iso", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
salixInstalledSWMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2158, 2, 4))
if mibBuilder.loadTexts: salixInstalledSWMIB.setLastUpdated('9810130000Z')
if mibBuilder.loadTexts: salixInstalledSWMIB.setOrganization('SALIX Technologies')
if mibBuilder.loadTexts: salixInstalledSWMIB.setContactInfo('904 Wind River Lane Suite 101 Gaithersburg, MD 20878 (301)-417-0017')
if mibBuilder.loadTexts: salixInstalledSWMIB.setDescription('The MIB describing Installed Software objects for SALIX products')
salixInstalledSWMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1))
salixInstalledSWMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 4, 2))
salixInstalledSWMIBCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 4, 3))
salixInstalledSWMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 4, 2, 0))
salixSysHrSWInstalledTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1), )
if mibBuilder.loadTexts: salixSysHrSWInstalledTable.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledTable.setDescription('The system installed software table. This table augments the hrSWInstalledTable to include additional attributes of the software installed in the table.')
salixSysHrSWInstalledEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1), )
hrSWInstalledEntry.registerAugmentions(("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysHrSWInstalledEntry"))
salixSysHrSWInstalledEntry.setIndexNames(*hrSWInstalledEntry.getIndexNames())
if mibBuilder.loadTexts: salixSysHrSWInstalledEntry.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledEntry.setDescription('An entry in the salixSysHrSWInstalledTable that describes additional attributes of the software installed in the hrSWInstalledTable.')
salixSysHrSWInstalledFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWInstalledFileVersion.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledFileVersion.setDescription('The release version of the software file installed in the software table entry.')
salixSysHrSWInstalledFileControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWInstalledFileControl.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledFileControl.setDescription('The date and time configuration and control information that uniquely identifies the file in the installed software table entry.')
salixSysHrSWInstalledFileCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWInstalledFileCreation.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledFileCreation.setDescription('The creation date and time of the file in the installed software table entry.')
salixSysHrSWInstalledFilePiuType = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 4), SalixPlugInUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWInstalledFilePiuType.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledFilePiuType.setDescription('The type of plugin unit that the installed software can operate.')
salixSysHrSWInstalledFileBuilderName = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWInstalledFileBuilderName.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledFileBuilderName.setDescription('The username of the person who created the file in the installed software table entry.')
salixSysHrSWInstalledFileReleaseLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWInstalledFileReleaseLabel.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWInstalledFileReleaseLabel.setDescription('The version control release label for the file in the installed software table entry .')
salixSysSwDownloadTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2), )
if mibBuilder.loadTexts: salixSysSwDownloadTable.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadTable.setDescription('The software download table. This table provides a mechanism for downloading software to the system. Software that is successfully downloaded is installed on the system and occupies an entry in the salixSysHrSWInstalledTable.')
salixSysSwDownloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrSWInstalledIndex"))
if mibBuilder.loadTexts: salixSysSwDownloadEntry.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadEntry.setDescription('An entry in the salixSysSwDownloadTable that identifies the parameters necessary to download software to the system.')
salixSysSwDownloadIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixSysSwDownloadIpAddress.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadIpAddress.setDescription('The Ip Address where the salixSysSwDownloadFilename object resides.')
salixSysSwDownloadFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixSysSwDownloadFilename.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadFilename.setDescription('The fully qualified filename found at the specified Ip Address (salixSysSwDownloadIpAddress) that is to be downloaded to the entry in the Table.')
salixSysSwDownloadUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixSysSwDownloadUsername.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadUsername.setDescription('The username to be used when getting a file from the computer at the IP address indicated by the salixSysSwDownloadIpAddress attribute. For security reasons, reading this field will return an empty string.')
salixSysSwDownloadPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixSysSwDownloadPassword.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadPassword.setDescription('The password to be used when getting a file from the computer at the IP address indicated by the salixSysSwDownloadIpAddress attribute. For security reasons, reading this field will return an empty string.')
salixSysSwDownloadRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("start", 1))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: salixSysSwDownloadRequest.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadRequest.setDescription("Setting this attribute to 'start' will cause the download request to begin.")
salixSysSwDownloadState = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("none", 1), ("inProgress", 2), ("success", 3), ("aborted", 4), ("failed", 5), ("locked", 6))).clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysSwDownloadState.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadState.setDescription('The state of the download software request. none(1) - download not started or not supported inProgress(2) - download in progress success(3) - download to the installed software table was successful. aborted(4) - download aborted failed(5) - download to at least one plug-in unit failed locked(6) - the filename in the installed software entry is locked by the management processor software.')
salixSysSwDownloadStatusMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysSwDownloadStatusMessage.setStatus('current')
if mibBuilder.loadTexts: salixSysSwDownloadStatusMessage.setDescription("Status message that describes the current state of the download as indicated by the 'salixSysSwDownloadState' attribute.")
salixSysHrSWRunTable = MibTable((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3), )
if mibBuilder.loadTexts: salixSysHrSWRunTable.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunTable.setDescription('The system Run software table. This table augments the hrSWRunTable to include additional attributes of the software Run in the table.')
salixSysHrSWRunEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1), )
hrSWRunEntry.registerAugmentions(("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysHrSWRunEntry"))
salixSysHrSWRunEntry.setIndexNames(*hrSWRunEntry.getIndexNames())
if mibBuilder.loadTexts: salixSysHrSWRunEntry.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunEntry.setDescription('An entry in the salixSysHrSWRunTable that describes additional attributes of the software Run in the hrSWRunTable.')
salixSysHrSWRunFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWRunFileVersion.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunFileVersion.setDescription('The release version of the software file Run in the software table entry.')
salixSysHrSWRunFileControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWRunFileControl.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunFileControl.setDescription('The date and time configuration and control information that uniquely identifies the file in the Run software table entry.')
salixSysHrSWRunFileCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWRunFileCreation.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunFileCreation.setDescription('The creation date and time of the file in the Run software table entry.')
salixSysHrSWRunFileBuilderName = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWRunFileBuilderName.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunFileBuilderName.setDescription('The username of the person who created the file in the Run software table entry.')
salixSysHrSWRunFileReleaseLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2158, 2, 4, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: salixSysHrSWRunFileReleaseLabel.setStatus('current')
if mibBuilder.loadTexts: salixSysHrSWRunFileReleaseLabel.setDescription('The version control release label for the file in the Run software table entry .')
salixInstalledSWGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 1))
salixInstalledSWCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 2))
salixInstalledSWGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 1, 1)).setObjects(("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadIpAddress"), ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadFilename"), ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadUsername"), ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadPassword"), ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadRequest"), ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadState"), ("SALIX-INSTALLED-SOFTWARE-MIB", "salixSysSwDownloadStatusMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixInstalledSWGroup = salixInstalledSWGroup.setStatus('current')
if mibBuilder.loadTexts: salixInstalledSWGroup.setDescription('Salix InstalledSW Objects Group')
salixInstalledSWCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2158, 2, 4, 3, 2, 1)).setObjects(("SALIX-INSTALLED-SOFTWARE-MIB", "salixInstalledSWGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    salixInstalledSWCompliance = salixInstalledSWCompliance.setStatus('current')
if mibBuilder.loadTexts: salixInstalledSWCompliance.setDescription('The basic implementation requirements for the SALIX-INSTALLED-SOFTWARE-MIB.')
mibBuilder.exportSymbols("SALIX-INSTALLED-SOFTWARE-MIB", salixSysHrSWInstalledFileBuilderName=salixSysHrSWInstalledFileBuilderName, salixSysHrSWInstalledTable=salixSysHrSWInstalledTable, salixSysSwDownloadStatusMessage=salixSysSwDownloadStatusMessage, salixSysHrSWInstalledEntry=salixSysHrSWInstalledEntry, salixSysHrSWRunFileBuilderName=salixSysHrSWRunFileBuilderName, PYSNMP_MODULE_ID=salixInstalledSWMIB, salixSysHrSWRunFileVersion=salixSysHrSWRunFileVersion, salixInstalledSWMIBCompliance=salixInstalledSWMIBCompliance, salixSysSwDownloadState=salixSysSwDownloadState, salixInstalledSWCompliance=salixInstalledSWCompliance, salixInstalledSWGroups=salixInstalledSWGroups, salixInstalledSWMIBTrapPrefix=salixInstalledSWMIBTrapPrefix, salixInstalledSWCompliances=salixInstalledSWCompliances, salixInstalledSWGroup=salixInstalledSWGroup, salixSysHrSWInstalledFileReleaseLabel=salixSysHrSWInstalledFileReleaseLabel, salixInstalledSWMIBTraps=salixInstalledSWMIBTraps, salixSysSwDownloadIpAddress=salixSysSwDownloadIpAddress, salixSysSwDownloadUsername=salixSysSwDownloadUsername, salixSysSwDownloadPassword=salixSysSwDownloadPassword, salixSysHrSWInstalledFileVersion=salixSysHrSWInstalledFileVersion, salixSysSwDownloadRequest=salixSysSwDownloadRequest, salixInstalledSWMIBObjects=salixInstalledSWMIBObjects, salixSysHrSWInstalledFileCreation=salixSysHrSWInstalledFileCreation, salixSysSwDownloadTable=salixSysSwDownloadTable, salixSysHrSWRunFileControl=salixSysHrSWRunFileControl, salixSysHrSWRunEntry=salixSysHrSWRunEntry, salixSysHrSWRunFileReleaseLabel=salixSysHrSWRunFileReleaseLabel, salixSysHrSWInstalledFilePiuType=salixSysHrSWInstalledFilePiuType, salixSysHrSWRunTable=salixSysHrSWRunTable, salixSysSwDownloadFilename=salixSysSwDownloadFilename, salixSysSwDownloadEntry=salixSysSwDownloadEntry, salixSysHrSWInstalledFileControl=salixSysHrSWInstalledFileControl, salixSysHrSWRunFileCreation=salixSysHrSWRunFileCreation, salixInstalledSWMIB=salixInstalledSWMIB)
