#
# PySNMP MIB module CISCO-CDSTV-INGESTMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDSTV-INGESTMGR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalMin, TimeIntervalSec, CiscoURLString, CiscoURLStringOrEmpty = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalMin", "TimeIntervalSec", "CiscoURLString", "CiscoURLStringOrEmpty")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, Bits, NotificationType, IpAddress, ObjectIdentity, Integer32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "NotificationType", "IpAddress", "ObjectIdentity", "Integer32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter32", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoCdstvIngestmgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 739))
ciscoCdstvIngestmgrMIB.setRevisions(('2010-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdstvIngestmgrMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdstvIngestmgrMIB.setLastUpdated('201005270000Z')
if mibBuilder.loadTexts: ciscoCdstvIngestmgrMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdstvIngestmgrMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cds@cisco.com')
if mibBuilder.loadTexts: ciscoCdstvIngestmgrMIB.setDescription("This MIB module defines ingest manager configuration objects that faciliate the management of the Cisco Content Delivery System for TV (CDS-TV) product family. CDS-TV is a suite of products and software applications providing ingest, storage, caching, streaming, playout and on-demand delivery of video to television or set-top-box clients. Abbreviations: CCP Cache Control Protocol CDS Content Delivery System CORBA Common Object Request Broker Architecture ISA Interactive Services Architecture ISV Integrated Streamer-Vault FSI File Service Interface FTP File Transfer Protocol MPEG Motion Picture Experts Group MSA Managed Services Architecture RTSP Real-Time Streaming Protocol STB Set-Top Box Common terms: Catcher: Device responsible for receiving content (typically via satellite dishes and antennae) from content providers or from a Headend-In-The-Sky. Content Ingest: Acquisition of content from a source such as a catcher or an FTP server for storing it locally and making it available to streamers as needed. Ingest Manager: CDS module that takes care of provisioned content objects by collecting metadata, sending messages to the appropriate subsystem to ingest the content, and sending messages to expire the content when the expiration period has passed. Device Roles: Vault: Content delivery application responsible for ingesting and storing video content and making it available to streamers and/or caching nodes. Caching Nodes: Content delivery application responsible for caching content from vault (using CCP) and then streaming content out to streamers over HTTP or CCP. Streamer: Content delivery application responsible for streaming video out to STB's. ISV: Content delivery application capable of acting as both a vault and as a streamer in a single device.")
ciscoCdstvIngestMgrMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 0))
ciscoCdstvIngestMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 1))
ciscoCdstvIngestMgrMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 2))
ciscoCdstvIngestMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 1))
cdstvIngestMgrGeneralSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1))
cdstvIngestMgrIngestSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2))
cdstvIngestMgrBackOfficeSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3))
cdstvIngestMgrContentStoreSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 4))
cdstvIngestMgrEncryptionSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5))
cdstvIngestMgrHostAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrHostAddressType.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrHostAddressType.setDescription('This object specifies the type of the IP address (specified by cdstvIngestMgrHostAddress) of the Ingest Manager.')
cdstvIngestMgrHostAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrHostAddress.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrHostAddress.setDescription('This object specifies the IP address of the Ingest Manager. The type of this address is specified by cdstvIngestMgrHostAddressType.')
cdstvIngestMgrPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 3), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrPort.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrPort.setDescription('This object specifies the port number to use for listening for inbound connections.')
cdstvIngestMgrFsiCallbackPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 4), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrFsiCallbackPort.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrFsiCallbackPort.setDescription('This object specifies the port number to use for File Services Interface (FSI) callbacks.')
cdstvIngestMgrAdditionalPackageWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 5), Unsigned32()).setUnits('days').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrAdditionalPackageWindow.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrAdditionalPackageWindow.setDescription('This object specifies the additional amount of time to wait once the package expiration window has ended before destroying the stored content package. Typically, when the package expiration window ends, the ingested content package is destroyed from the device. The additional package window adds a grace period to the expiration window.')
cdstvIngestMgrFtpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 6), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrFtpTimeout.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrFtpTimeout.setDescription('This object specifies the maximum period the Ingest Manager waits before timing out an FTP session and terminating the process.')
cdstvIngestMgrUseAssetIdEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrUseAssetIdEnable.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrUseAssetIdEnable.setDescription("This object specifies whether to use the Asset ID (a unique ID assigned to each content ingested into the CDS) for the content name. 'true' indicates that Asset ID is used for the content name. 'false' indicates Asset ID is not used for the content name.")
cdstvIngestMgrManageCorbaServices = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrManageCorbaServices.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrManageCorbaServices.setDescription("This object specifies whether the CDS manages the CORBA services. 'true' indicates that CDS manages CORBA services. 'false' indicates that CDS does not manage CORBA services.")
cdstvIngestMgrRequireNotifyService = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrRequireNotifyService.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrRequireNotifyService.setDescription("This object specifies whether the CDS requires the use of ISA Notify Service. 'true' indicates that CDS requires the use of ISA Notify Service. 'false' indicates that CDS does not require the use of ISA Notify Service.")
cdstvIngestMgrDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("errors", 1), ("all", 2), ("off", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrDebugLevel.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrDebugLevel.setDescription('This object specifies the amount of debugging information logged. errors(1) - Only error messages are logged. all(2) - Errors, warnings and success message are all logged. off(3) - Debugging is disabled.')
cdstvIngestMgrMetaDataPublish = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrMetaDataPublish.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrMetaDataPublish.setDescription("This object specifies whether content metadata is published or not. 'true' indicates that content metadata is published. 'false' indicates that content metadata is not published.")
cdstvIngestMgrMetaPublishUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 12), CiscoURLString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrMetaPublishUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrMetaPublishUrl.setDescription('This object specifies the URL where the metadata is published, typically the back-office.')
cdstvIngestMgrMetaPublishBackupUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 1, 13), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrMetaPublishBackupUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrMetaPublishBackupUrl.setDescription('This object specifies the URL of the backup server where the metadata is published. This string is empty if a backup server URL is not configured.')
cdstvIngestMgrIngestInterface = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2, 1), Bits().clone(namedValues=NamedValues(("isa", 0), ("ciscoSoap", 1), ("prodisSoap", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrIngestInterface.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrIngestInterface.setDescription('This object specifies all ingest interfaces (methods) available, i.e. ISA, Cisco SOAP, Prodis SOAP or any combination of the three. isa(0) - ISA. ciscoSoap(1) - Cisco SOAP prodisSoap(2) - Prodis SOAP.')
cdstvIngestMgrCiscoSoapUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2, 2), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrCiscoSoapUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrCiscoSoapUrl.setDescription('This object specifies the URL (IP address, port, and directory) on the Vault used to receive content using the Cisco SOAP (Simple Object Access Protocol). An example of the Cisco SOAP URL is http://10.22.216.251:8793/CiscoAIM. This string is empty if Cisco SOAP is not used.')
cdstvIngestMgrProdisSoapUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 2, 3), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrProdisSoapUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrProdisSoapUrl.setDescription('This object specifies the URL (IP address, port, and directory) on the Vault used to receive content using the Prodis SOAP(Simple Object Access Protocol). An example of the Prodis SOAP URL is http://10.22.216.251:8793/ProdisAIM. This string is empty if Prodis SOAP is not used.')
cdstvIngestMgrBackOfficeMaxRetries = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeMaxRetries.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeMaxRetries.setDescription('This object specifies the maximum number of times to retry a failed communication with the back-office.')
cdstvIngestMgrBackOfficeRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 2), TimeIntervalMin()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeRetryInterval.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeRetryInterval.setDescription('This object specifies the amount of time to wait before retrying a failed communication with the back-office.')
cdstvIngestMgrBackOfficeTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 3), TimeIntervalSec()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeTimeout.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeTimeout.setDescription('This object specifies the amount of time to wait for the back-office to respond to a communication attempt.')
cdstvIngestMgrBackOfficeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4), )
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeTable.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeTable.setDescription('A table containing the back-office type and URL settings.')
cdstvIngestMgrBackOfficeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1), ).setIndexNames((0, "CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeIndex"))
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeEntry.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeEntry.setDescription('An entry (conceptual row) in the table of back-office type and URL settings. Rows are added if new back-offices are configured and deleted if back-offices are disabled.')
cdstvIngestMgrBackOfficeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeIndex.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeIndex.setDescription('This object uniquely identifies a back-office.')
cdstvIngestMgrBackOfficeType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("totalManage", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeType.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeType.setDescription('This object specifies the type of back-office support used. none(1) - No back-office support. totalManage(2) - Use TotalManage back-office support.')
cdstvIngestMgrBackOfficeUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 3, 4, 1, 3), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrBackOfficeUrl.setDescription('This object specifies the location (URL) of the back-office. This string is empty if back-office support is disabled.')
cdstvIngestMgrContentStore = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("isa", 2), ("fsi", 3), ("ngod", 4), ("openStream", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrContentStore.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrContentStore.setDescription('This object specifies the type of content store used. none(1) - Content store is disabled. isa(2) - Use ISA content store. fsi(3) - Use FSI content store. ngod(4) - Use Next-Generation On-Demand (NGOD) content store. openStream(5) - Use OpenStream content store.')
cdstvIngestMgrContentStoreUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 4, 2), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrContentStoreUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrContentStoreUrl.setDescription('This object specifies the URL where the content store is located. This string is empty if content store is disabled.')
cdstvIngestMgrEncryptionType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("verimatrix", 2), ("widevine", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrEncryptionType.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrEncryptionType.setDescription('This object specifies the type of encryption used. none(1) - Encryption is disabled. verimatrix(2) - Use Verimatrix encryption. widevine(3) - Use Widevine encryption.')
cdstvIngestMgrEncryptionTargetUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5, 2), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrEncryptionTargetUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrEncryptionTargetUrl.setDescription('This object specifies the location on the encryption server used to send MPEG files for encryption, for example, http://192.168.128.54:7898/files/encrypted. This string will be empty if encryption is disabled.')
cdstvIngestMgrEncryptionRetrievalUrl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 739, 1, 5, 3), CiscoURLStringOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvIngestMgrEncryptionRetrievalUrl.setStatus('current')
if mibBuilder.loadTexts: cdstvIngestMgrEncryptionRetrievalUrl.setDescription('This object specifies the location on the encryption server used to retrieve encrypted MPEG files, for example, ftp://192.168.128.54:7899/files/encrypted. This string will be empty if encryption is disabled.')
ciscoCdstvIngestMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2))
ciscoCdstvIngestMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 1, 1)).setObjects(("CISCO-CDSTV-INGESTMGR-MIB", "ciscoCdstvIngestMgrMIBMainObjectGroup"), ("CISCO-CDSTV-INGESTMGR-MIB", "ciscoCdstvIngestMgrMIBIngestSettingsGroup"), ("CISCO-CDSTV-INGESTMGR-MIB", "ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup"), ("CISCO-CDSTV-INGESTMGR-MIB", "ciscoCdstvIngestMgrMIBContentStoreSettingsGroup"), ("CISCO-CDSTV-INGESTMGR-MIB", "ciscoCdstvIngestMgrMIBEncryptionSettingsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestMgrMIBCompliance = ciscoCdstvIngestMgrMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestMgrMIBCompliance.setDescription('The compliance statement for the entities which implement the Cisco CDS TV Ingest Manager MIB.')
ciscoCdstvIngestMgrMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 1)).setObjects(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrHostAddress"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrPort"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrFsiCallbackPort"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrAdditionalPackageWindow"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrFtpTimeout"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrUseAssetIdEnable"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrManageCorbaServices"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrRequireNotifyService"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrDebugLevel"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrMetaDataPublish"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrMetaPublishUrl"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrMetaPublishBackupUrl"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrHostAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestMgrMIBMainObjectGroup = ciscoCdstvIngestMgrMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestMgrMIBMainObjectGroup.setDescription('A collection of objects that provide the configuration of CDS-TV ingest manager.')
ciscoCdstvIngestMgrMIBIngestSettingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 2)).setObjects(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrIngestInterface"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrCiscoSoapUrl"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrProdisSoapUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestMgrMIBIngestSettingsGroup = ciscoCdstvIngestMgrMIBIngestSettingsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestMgrMIBIngestSettingsGroup.setDescription('A collection of objects that provide the ingest settings of the CDS-TV ingest manager.')
ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 3)).setObjects(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeMaxRetries"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeRetryInterval"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeTimeout"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeType"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrBackOfficeUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup = ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup.setDescription('A collection of objects that provide the back-office settings of the CDS-TV ingest manager.')
ciscoCdstvIngestMgrMIBContentStoreSettingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 4)).setObjects(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrContentStore"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrContentStoreUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestMgrMIBContentStoreSettingsGroup = ciscoCdstvIngestMgrMIBContentStoreSettingsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestMgrMIBContentStoreSettingsGroup.setDescription('A collection of objects that provide the content store settings of the CDS-TV ingest manager.')
ciscoCdstvIngestMgrMIBEncryptionSettingsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 739, 2, 2, 5)).setObjects(("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrEncryptionType"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrEncryptionTargetUrl"), ("CISCO-CDSTV-INGESTMGR-MIB", "cdstvIngestMgrEncryptionRetrievalUrl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestMgrMIBEncryptionSettingsGroup = ciscoCdstvIngestMgrMIBEncryptionSettingsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestMgrMIBEncryptionSettingsGroup.setDescription('A collection of objects that provide the encryption settings of the CDS-TV ingest manager.')
mibBuilder.exportSymbols("CISCO-CDSTV-INGESTMGR-MIB", cdstvIngestMgrFtpTimeout=cdstvIngestMgrFtpTimeout, cdstvIngestMgrDebugLevel=cdstvIngestMgrDebugLevel, ciscoCdstvIngestMgrMIBConform=ciscoCdstvIngestMgrMIBConform, cdstvIngestMgrManageCorbaServices=cdstvIngestMgrManageCorbaServices, cdstvIngestMgrContentStoreUrl=cdstvIngestMgrContentStoreUrl, cdstvIngestMgrEncryptionType=cdstvIngestMgrEncryptionType, cdstvIngestMgrUseAssetIdEnable=cdstvIngestMgrUseAssetIdEnable, cdstvIngestMgrFsiCallbackPort=cdstvIngestMgrFsiCallbackPort, cdstvIngestMgrBackOfficeEntry=cdstvIngestMgrBackOfficeEntry, cdstvIngestMgrBackOfficeIndex=cdstvIngestMgrBackOfficeIndex, cdstvIngestMgrBackOfficeUrl=cdstvIngestMgrBackOfficeUrl, cdstvIngestMgrMetaPublishUrl=cdstvIngestMgrMetaPublishUrl, cdstvIngestMgrBackOfficeTimeout=cdstvIngestMgrBackOfficeTimeout, ciscoCdstvIngestMgrMIBContentStoreSettingsGroup=ciscoCdstvIngestMgrMIBContentStoreSettingsGroup, cdstvIngestMgrEncryptionSettings=cdstvIngestMgrEncryptionSettings, ciscoCdstvIngestMgrMIBCompliances=ciscoCdstvIngestMgrMIBCompliances, cdstvIngestMgrAdditionalPackageWindow=cdstvIngestMgrAdditionalPackageWindow, cdstvIngestMgrBackOfficeSettings=cdstvIngestMgrBackOfficeSettings, cdstvIngestMgrMetaPublishBackupUrl=cdstvIngestMgrMetaPublishBackupUrl, cdstvIngestMgrBackOfficeMaxRetries=cdstvIngestMgrBackOfficeMaxRetries, ciscoCdstvIngestMgrMIBIngestSettingsGroup=ciscoCdstvIngestMgrMIBIngestSettingsGroup, PYSNMP_MODULE_ID=ciscoCdstvIngestmgrMIB, cdstvIngestMgrRequireNotifyService=cdstvIngestMgrRequireNotifyService, cdstvIngestMgrBackOfficeTable=cdstvIngestMgrBackOfficeTable, ciscoCdstvIngestMgrMIBEncryptionSettingsGroup=ciscoCdstvIngestMgrMIBEncryptionSettingsGroup, cdstvIngestMgrEncryptionRetrievalUrl=cdstvIngestMgrEncryptionRetrievalUrl, cdstvIngestMgrContentStoreSettings=cdstvIngestMgrContentStoreSettings, ciscoCdstvIngestMgrMIBNotifs=ciscoCdstvIngestMgrMIBNotifs, ciscoCdstvIngestMgrMIBObjects=ciscoCdstvIngestMgrMIBObjects, cdstvIngestMgrIngestSettings=cdstvIngestMgrIngestSettings, cdstvIngestMgrBackOfficeType=cdstvIngestMgrBackOfficeType, ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup=ciscoCdstvIngestMgrMIBBackOfficeSettingsGroup, cdstvIngestMgrProdisSoapUrl=cdstvIngestMgrProdisSoapUrl, cdstvIngestMgrEncryptionTargetUrl=cdstvIngestMgrEncryptionTargetUrl, cdstvIngestMgrBackOfficeRetryInterval=cdstvIngestMgrBackOfficeRetryInterval, cdstvIngestMgrContentStore=cdstvIngestMgrContentStore, ciscoCdstvIngestMgrMIBMainObjectGroup=ciscoCdstvIngestMgrMIBMainObjectGroup, cdstvIngestMgrHostAddress=cdstvIngestMgrHostAddress, cdstvIngestMgrPort=cdstvIngestMgrPort, cdstvIngestMgrIngestInterface=cdstvIngestMgrIngestInterface, cdstvIngestMgrHostAddressType=cdstvIngestMgrHostAddressType, cdstvIngestMgrMetaDataPublish=cdstvIngestMgrMetaDataPublish, cdstvIngestMgrGeneralSettings=cdstvIngestMgrGeneralSettings, ciscoCdstvIngestMgrMIBCompliance=ciscoCdstvIngestMgrMIBCompliance, ciscoCdstvIngestMgrMIBGroups=ciscoCdstvIngestMgrMIBGroups, cdstvIngestMgrCiscoSoapUrl=cdstvIngestMgrCiscoSoapUrl, ciscoCdstvIngestmgrMIB=ciscoCdstvIngestmgrMIB)
