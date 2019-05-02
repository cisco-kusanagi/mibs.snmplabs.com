#
# PySNMP MIB module CISCO-WAN-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-MODULE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:20:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Counter64, NotificationType, TimeTicks, ObjectIdentity, Integer32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "NotificationType", "TimeTicks", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanModuleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 145))
ciscoWanModuleMIB.setRevisions(('2002-09-11 00:00', '2001-07-20 00:00', '1999-10-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanModuleMIB.setRevisionsDescriptions(('Imported Unsigned32 from SNMPv2-SMI instead of CISCO-TC. Added cwmUploadCounter in cwmConfigTable.', ' 1. Added cwmSCTFileVerCfg and cwmSCTFileVerOpr to CwmConfigEntry. ', 'Initial version of the mib module.',))
if mibBuilder.loadTexts: ciscoWanModuleMIB.setLastUpdated('200209110000Z')
if mibBuilder.loadTexts: ciscoWanModuleMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanModuleMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanModuleMIB.setDescription('The MIB to configure Connection Specific parameters and statistics related information in a Service Module. The Service Module(SM) is defined as any Module which provides services such as ATM, Frame Relay or Voice in a Wide Area Network(WAN) switch.')
cwmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1))
cwmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1))
cwmStatsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2))
class StatisticsLevel(TextualConvention, Integer32):
    description = 'Used to configure level statistics on service module. Statistic level on a module dictates the type and amount of statistics that is collected. There is a predefined set of statistics associated with each level and are enabled when a level is set. Also, setting statistics level to N will enable counters associated with levels N-1 through 1 as well. The valid values are notApplicable(0)- Statistics level is not applicable. levelOne(1) - Enables level one counters. levelTwo(2) - Enables level two and level one counters. levelThree(3) - Enables level one, level two and level three counters.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("levelOne", 1), ("levelTwo", 2), ("levelThree", 3))

cwmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1), )
if mibBuilder.loadTexts: cwmConfigTable.setStatus('current')
if mibBuilder.loadTexts: cwmConfigTable.setDescription('This table contains objects required for configuring module specific parameters. These parameters may be related to the hardware specific parameters which can affect the ATM Connection characteristics.')
cwmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-MODULE-MIB", "cwmIndex"))
if mibBuilder.loadTexts: cwmConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cwmConfigEntry.setDescription('Entry containing information for each module.')
cwmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cwmIndex.setStatus('current')
if mibBuilder.loadTexts: cwmIndex.setDescription("This object's value generally corresponds to the slot number where the module resides. However, system wide uniqueness is the only true requirement.")
cwmIngressSCTFileId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmIngressSCTFileId.setStatus('current')
if mibBuilder.loadTexts: cwmIngressSCTFileId.setDescription('The file ID of the Service Class Template(SCT) file. The SCT holds the connection specific parameters for this module in the ingress direction(From Network to the Switch). Terminologies used: SCT : Service Class Template The Service Class Template ( or Service Template or SCT ) provides a means for inferring extended parameters, which are generally platform-specific, from the set of standard ATM protocol parameters passed in VSI(Virtual Switch Interface) connection setup primitives. A set of Service Templates are available in a non-volatile storage and is downloaded onto each Service Module on power up. In general, SCTs contain two classes of data. One class consists of parameters necessary to establish a Virtual Connection (i.e. Per-VC) and includes entries such as UPC(Usage Parameter Control) actions, various bandwidth-related items, per-VC thresholds, and some hardware-specific items.The second class of data items includes those necessary to configure the associated Class-of-Service Buffers that provide the QoS support.')
cwmIngressSCTFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmIngressSCTFileName.setStatus('current')
if mibBuilder.loadTexts: cwmIngressSCTFileName.setDescription('This variable contains the SCT filename. Write access is not required. The filename has cwmIngressSCTFileId value as the suffix. For example, the value SCT.INGR.13 for this object indicates 13 is the value of cwmIngressSCTFileId.')
cwmAutoLineDiagEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmAutoLineDiagEnable.setStatus('current')
if mibBuilder.loadTexts: cwmAutoLineDiagEnable.setDescription('This object enables/disables automatic diagnostic feature of physical lines on module. In case of a line alarm, enabling this feature temporarily suspends traffic in both direction and starts local loop-back testing. Disabling this feature will not effect the traffic in one direction while another direction is in alarm.')
cwmSCTFileVerCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmSCTFileVerCfg.setStatus('current')
if mibBuilder.loadTexts: cwmSCTFileVerCfg.setDescription('The Configured version of the Service Class Template(SCT) file. This version applies to both the card SCT and the port SCT files in a service module. The port SCT files are specified while provisioning a port using the caviFileId field in the CISCO-WAN-VIRTUAL-IF-MIB.my MIB. The card SCT file is specifed in this MIB using the cwmIngressSCTFileName object. The configured version of the SCT does not take effect until the service module is rebooted. However, graceful invocation of a new SCT version can be achieved by using redundant service modules. The configured SCT version is first applied on a standby service module by rebooting it. When the standby reboots, it comes up with the configured SCT version. Thereafter a switchover can be performed, making the standby SM take over as active.')
cwmSCTFileVerOpr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmSCTFileVerOpr.setStatus('current')
if mibBuilder.loadTexts: cwmSCTFileVerOpr.setDescription('The operational version of the Service Class Template(SCT) file. This is sct version currently in use. The operational version could be different from the configured version (cwmSCTFileVerCfg), until the service module is rebooted.')
cwmUploadCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmUploadCounter.setStatus('current')
if mibBuilder.loadTexts: cwmUploadCounter.setDescription('This counter is used by the management station to determine if any changes(other than ATM/FR connections) have been done on configuration of a card. The use of this object is implementation specific. This requires the NMS application saving the previous value of this object and compare it later for finding any changes in the card. The upload counter is incremented in, for instance: - any physical interface characteristics are modified. - any logical interface is added/deleted/modified. - any IMA Group/MFR bundle is added/deleted/modified. - any resource is added/deleted/modified on an interface. - any configuration changes are done(not specified above) which are not related to ATM/FR Connections (SPVCs for example).')
cwmStatConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1), )
if mibBuilder.loadTexts: cwmStatConfigTable.setStatus('current')
if mibBuilder.loadTexts: cwmStatConfigTable.setDescription("This table has objects required for configuring module statistic collection related parameters. The statistics related to interfaces and ATM Connections are stored in a file. The statistics file can be uploaded by NMS applications using file transfer protocols such as tftp or ftp. While current interval of data is being collected in memory, previous interval of data is uploaded by NMS. Each interval's data will overwrite the previous interval's data in the statistic file after the interval is over.")
cwmStatConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-MODULE-MIB", "cwmIndex"))
if mibBuilder.loadTexts: cwmStatConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cwmStatConfigEntry.setDescription('Entry containing statistics configuration information for the module.')
cwmStatBucketInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10, 15, 20, 30, 60))).clone(namedValues=NamedValues(("five", 5), ("ten", 10), ("fifteen", 15), ("twenty", 20), ("thirty", 30), ("sixty", 60))).clone('fifteen')).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatBucketInterval.setStatus('current')
if mibBuilder.loadTexts: cwmStatBucketInterval.setDescription('This object contains the bucket interval in minutes used in collecting statistics. This specifies the interval over which the module accumulates a sample. This value also defines the amount of time available to NMS application to upload the statistic file in order to not miss one interval worth of data.')
cwmStatCollectionInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 5))).clone(namedValues=NamedValues(("default", 0), ("one", 1), ("five", 5))).clone('default')).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatCollectionInterval.setStatus('current')
if mibBuilder.loadTexts: cwmStatCollectionInterval.setDescription('The collection interval of statistics. Within a sampling interval, as defined by cwmStatBucketInterval, statistics counters are updated every collection interval. Default value of collection interval is same as bucket interval. In case of bucket interval being 5 minutes, default(0) and five(5) values for this object has the same effect.')
cwmStatCollectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatCollectionStatus.setStatus('current')
if mibBuilder.loadTexts: cwmStatCollectionStatus.setDescription('Enables or disables statistics collection on the module.')
cwmStatCurrentLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 4), StatisticsLevel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmStatCurrentLevel.setStatus('current')
if mibBuilder.loadTexts: cwmStatCurrentLevel.setDescription('The current statistics level of the module. A change in the card statistic level can take place only after a module reset. This object shows the current module statistic level. While cwmStatLevelConfigured object is used to configure module statistic level. The value set in cwmStatLevelConfigured object will take effect after next module reset.')
cwmStatLevelConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 5), StatisticsLevel().clone('levelOne')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmStatLevelConfigured.setStatus('current')
if mibBuilder.loadTexts: cwmStatLevelConfigured.setDescription('This object is used to configure the statistics level for the module. The statistics level value set in this object will take effect only on reset of the module. This object can be set only if cwmStatCollectionStatus is set to enable(1). This object cannot be set to notApplicable(0).')
cwmStatMaximumConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwmStatMaximumConnections.setStatus('current')
if mibBuilder.loadTexts: cwmStatMaximumConnections.setDescription('The maximum number of connections for which the statistics are being collected.')
ciscoWanModuleMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 2))
ciscoWanModuleMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 2, 0))
ciscoWanModuleMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3))
ciscoWanModuleMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1))
ciscoWanModuleMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2))
ciscoWanModuleMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 1)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBCompliance = ciscoWanModuleMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoWanModuleMIBCompliance.setDescription('The Compliance statement for cwmConfigGroup group.')
ciscoWanModuleMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 2)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"), ("CISCO-WAN-MODULE-MIB", "cwmConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBComplianceRev1 = ciscoWanModuleMIBComplianceRev1.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoWanModuleMIBComplianceRev1.setDescription('The Compliance statement for cwmConfigGroup group, with addition of SCT file versioning ')
ciscoWanModuleMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 3)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmConfigGroup"), ("CISCO-WAN-MODULE-MIB", "cwmConfigGroup2"), ("CISCO-WAN-MODULE-MIB", "cwmUploadGroup"), ("CISCO-WAN-MODULE-MIB", "cwmStatConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleMIBComplianceRev2 = ciscoWanModuleMIBComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: ciscoWanModuleMIBComplianceRev2.setDescription('The Compliance statement for cwmConfigGroup group, with addition of SCT file versioning ')
cwmConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 1)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileId"), ("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileName"), ("CISCO-WAN-MODULE-MIB", "cwmAutoLineDiagEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmConfigGroup = cwmConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cwmConfigGroup.setDescription('Group containing Module Specific Parameters.')
cwmStatConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 2)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmStatBucketInterval"), ("CISCO-WAN-MODULE-MIB", "cwmStatCurrentLevel"), ("CISCO-WAN-MODULE-MIB", "cwmStatLevelConfigured"), ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionStatus"), ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionInterval"), ("CISCO-WAN-MODULE-MIB", "cwmStatMaximumConnections"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmStatConfigGroup = cwmStatConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cwmStatConfigGroup.setDescription('Group containing statistics configuration.')
cwmConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 3)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerCfg"), ("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerOpr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmConfigGroup2 = cwmConfigGroup2.setStatus('current')
if mibBuilder.loadTexts: cwmConfigGroup2.setDescription('Group containing additional Module Specific Parameters.')
cwmUploadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 4)).setObjects(("CISCO-WAN-MODULE-MIB", "cwmUploadCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmUploadGroup = cwmUploadGroup.setStatus('current')
if mibBuilder.loadTexts: cwmUploadGroup.setDescription('Group containing objects related to configuration changes in a card.')
mibBuilder.exportSymbols("CISCO-WAN-MODULE-MIB", ciscoWanModuleMIBConformance=ciscoWanModuleMIBConformance, cwmStatCollectionInterval=cwmStatCollectionInterval, cwmConfigGroup2=cwmConfigGroup2, ciscoWanModuleMIBCompliances=ciscoWanModuleMIBCompliances, cwmStatConfigTable=cwmStatConfigTable, cwmStatConfigGroup=cwmStatConfigGroup, cwmIngressSCTFileId=cwmIngressSCTFileId, ciscoWanModuleMIBCompliance=ciscoWanModuleMIBCompliance, cwmMIBObjects=cwmMIBObjects, cwmSCTFileVerOpr=cwmSCTFileVerOpr, cwmStatBucketInterval=cwmStatBucketInterval, cwmConfig=cwmConfig, ciscoWanModuleMIBNotifications=ciscoWanModuleMIBNotifications, cwmStatCollectionStatus=cwmStatCollectionStatus, ciscoWanModuleMIBComplianceRev2=ciscoWanModuleMIBComplianceRev2, StatisticsLevel=StatisticsLevel, cwmStatsConfig=cwmStatsConfig, cwmIndex=cwmIndex, cwmAutoLineDiagEnable=cwmAutoLineDiagEnable, cwmConfigEntry=cwmConfigEntry, cwmStatMaximumConnections=cwmStatMaximumConnections, cwmConfigTable=cwmConfigTable, ciscoWanModuleMIBGroups=ciscoWanModuleMIBGroups, cwmStatCurrentLevel=cwmStatCurrentLevel, cwmConfigGroup=cwmConfigGroup, cwmSCTFileVerCfg=cwmSCTFileVerCfg, cwmUploadGroup=cwmUploadGroup, cwmUploadCounter=cwmUploadCounter, PYSNMP_MODULE_ID=ciscoWanModuleMIB, cwmStatLevelConfigured=cwmStatLevelConfigured, ciscoWanModuleMIBComplianceRev1=ciscoWanModuleMIBComplianceRev1, cwmIngressSCTFileName=cwmIngressSCTFileName, ciscoWanModuleMIBNotificationPrefix=ciscoWanModuleMIBNotificationPrefix, ciscoWanModuleMIB=ciscoWanModuleMIB, cwmStatConfigEntry=cwmStatConfigEntry)
