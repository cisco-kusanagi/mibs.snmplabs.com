#
# PySNMP MIB module CISCO-RPMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RPMS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Bits, IpAddress, Counter64, Integer32, MibIdentifier, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Counter32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "IpAddress", "Counter64", "Integer32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "Gauge32")
DisplayString, RowStatus, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TimeStamp", "TextualConvention")
ciscoRpmsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 84))
ciscoRpmsMIB.setRevisions(('2002-04-17 00:00', '2001-11-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRpmsMIB.setRevisionsDescriptions(("Updated name from Resource Pool Manager Server to Resource Policy Management System (RPMS). This reflects product change, Corrected omission of 'crpmsVpdnGroupCpEntryStatus' from 'crpmsVpdnGroup' object group in initial release, Updated E-Mail contact to correct list for rpms.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRpmsMIB.setLastUpdated('200204170000Z')
if mibBuilder.loadTexts: ciscoRpmsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRpmsMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-rpms@cisco.com')
if mibBuilder.loadTexts: ciscoRpmsMIB.setDescription('This MIB contains objects pertinent to a Resource Policy Management System (RPMS) server. RPMS is a key component of Cisco Any Service Any Port (ASAP) solution and provides the ability to dynamically share resources across network access servers (NAS). RPMS enables enforcement of Service Level Agreements(SLA) between wholesale providers and their customers. Such SLA enforcement is done at call pre-authentication stage. An SLA is conceptually a set of clauses (limits) that dictate how voice, dial and/or virtual private data network (VPDN) services will be provided by the wholesaler. ')
ciscoRpmsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1))
crpmsSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1))
crpmsCustomerProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2))
crpmsVpdn = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3))
crpmsNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4))
crpmsSubsystemTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1), )
if mibBuilder.loadTexts: crpmsSubsystemTable.setStatus('current')
if mibBuilder.loadTexts: crpmsSubsystemTable.setDescription('This table contains currently working RPMS subsystems. Each row contains the name of the subsystem and its uptime since last initialization.')
crpmsSubsystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-RPMS-MIB", "crpmsSubsystemIndex"))
if mibBuilder.loadTexts: crpmsSubsystemEntry.setStatus('current')
if mibBuilder.loadTexts: crpmsSubsystemEntry.setDescription('A subsystem entry contains information of a RPMS subsystem. At the system startup, if a subsystem fails to initialize itself, it will not appear in this table. If a subsystem becomes unavailable, its corresponding row will be removed from this table.')
crpmsSubsystemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: crpmsSubsystemIndex.setStatus('current')
if mibBuilder.loadTexts: crpmsSubsystemIndex.setDescription('An unique value, greater than zero, for each subsystem. It is recommended that values are assigned contiguously starting from 1.')
crpmsSubsystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsSubsystemName.setStatus('current')
if mibBuilder.loadTexts: crpmsSubsystemName.setDescription('The name of the subsystem entry.')
crpmsSubsystemUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 1, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsSubsystemUptime.setStatus('current')
if mibBuilder.loadTexts: crpmsSubsystemUptime.setDescription('The time (in hundredths of a second) since the subsystem was last (re)initialized.')
crpmsCpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1), )
if mibBuilder.loadTexts: crpmsCpTable.setStatus('current')
if mibBuilder.loadTexts: crpmsCpTable.setDescription('The customer profile table contains information about all SLAs hosted on an SLA Server.')
crpmsCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1), ).setIndexNames((1, "CISCO-RPMS-MIB", "crpmsCpName"))
if mibBuilder.loadTexts: crpmsCpEntry.setStatus('current')
if mibBuilder.loadTexts: crpmsCpEntry.setDescription('A customer profile (Cp) entry contains information about a specific customer. A customer profile is a set of limits associated with a customer. These limits control how RPMS will respond to an incoming call under various scenarios.')
crpmsCpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsCpName.setStatus('current')
if mibBuilder.loadTexts: crpmsCpName.setDescription('The name of the customer profile. This name uniquely identifies the customer profile in the RPMS system.')
crpmsCpLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpLimit.setStatus('current')
if mibBuilder.loadTexts: crpmsCpLimit.setDescription('The maximum number of concurrent calls allowed in this customer profile. Once this limit is exceeded, RPMS will reject any new calls unless an overflow limit (crpmsCpOverflowLimit) is configured for this customer.')
crpmsCpOverflowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpOverflowLimit.setStatus('current')
if mibBuilder.loadTexts: crpmsCpOverflowLimit.setDescription('The maximum number of calls allowed after the customer profile limit(crpmsCpLimit) has been reached. Such calls are termed overflow calls.')
crpmsCpActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpActiveCalls.setStatus('current')
if mibBuilder.loadTexts: crpmsCpActiveCalls.setDescription('Number of current active calls for this customer profile.')
crpmsCpActiveOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpActiveOverflowCalls.setStatus('current')
if mibBuilder.loadTexts: crpmsCpActiveOverflowCalls.setDescription('Number of current active overflow calls for this customer profile.')
crpmsCpAttemptedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpAttemptedCalls.setStatus('current')
if mibBuilder.loadTexts: crpmsCpAttemptedCalls.setDescription('Total number of attempted calls (both successful and failed) for this customer profile.')
crpmsCpAttemptedOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpAttemptedOverflowCalls.setStatus('current')
if mibBuilder.loadTexts: crpmsCpAttemptedOverflowCalls.setDescription('Number of attempted overflow calls (both successful and failed) for this customer profile.')
crpmsCpRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpRejections.setStatus('current')
if mibBuilder.loadTexts: crpmsCpRejections.setDescription('Total number of rejected calls for this customer profile (crpmsCpOverflowRejections plus rejections due to unavailable resources).')
crpmsCpOverflowRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsCpOverflowRejections.setStatus('current')
if mibBuilder.loadTexts: crpmsCpOverflowRejections.setDescription('Number of rejected overflow calls for this customer profile.')
crpmsCpLimitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpLimitThreshold.setStatus('current')
if mibBuilder.loadTexts: crpmsCpLimitThreshold.setDescription('A threshold defined for the customer profile limit (crpmsCpLimit). It represents the percentage of the limit which, when crossed triggers a crpmsRisingAlarm or a crpmsFallingAlarm notification (refer to the notification definitions in this MIB for more details). A value of 100 percent cannot be exceeded and therefore disables this threshold setting. A value of 0 percent is always exceeded. ')
crpmsCpOverflowLimitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpOverflowLimitThreshold.setStatus('current')
if mibBuilder.loadTexts: crpmsCpOverflowLimitThreshold.setDescription('A threshold defined for the customer profile overflow limit (crpmsCpOverflowLimit). It represents the percentage of the limit that when exceeded triggers a crpmsRisingAlarm or a crpmsFallingAlarm notification (refer to the notification definitions in this MIB for more details). A value of 100 percent cannot be exceeded and therefore disables this threshold setting. A value of 0 percent is always exceeded. ')
crpmsCpCallRejectionThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpCallRejectionThreshold.setStatus('current')
if mibBuilder.loadTexts: crpmsCpCallRejectionThreshold.setDescription('A threshold defined for the number of customer profile rejected calls (crpmsCpRejections) as a percentage of the number of attempted calls (crpmsCpAttemptedCalls) which, when crossed, triggers a crpmsRisingAlarm or crpmsFallingAlarm notification (refer to the notification definitions in this MIB for more details). A value of 100 percent cannot be exceeded and therefore disables this threshold setting. A value of 0 percent is always exceeded. ')
crpmsCpOverflowRejectThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpOverflowRejectThreshold.setStatus('current')
if mibBuilder.loadTexts: crpmsCpOverflowRejectThreshold.setDescription('A threshold defined for the number of customer profile rejected overflow calls (crpmsCpOverflowRejections) as a percentage of the number of attempted overflow calls (crpmsCpAttemptedOverflowCalls) which, when crossed, triggers a crpmsRisingAlarm or a crpmsFallingAlarm notification (refer to the notification definitions in this MIB for more details). A value of 100 percent cannot be exceeded and therefore disables this threshold setting. A value of 0 percent is always exceeded. ')
crpmsCpEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 2, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsCpEntryStatus.setStatus('current')
if mibBuilder.loadTexts: crpmsCpEntryStatus.setDescription('Used to create, delete or modify this row. None of the columnar objects can be modified except this one, when the row is active.')
crpmsVpdnGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1), )
if mibBuilder.loadTexts: crpmsVpdnGroupTable.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupTable.setDescription('A VPDN group manages a number of sessions. A VPDN session may use a MLP link, which is contained within a particular MLP bundle. A VPDN group has a limit of maximal sessions, the number of bundles that this VPDN group can allocate, and the number of links for each bundle. The VPDN group table contains information about VPDN group of a RPMS server, each group a row. If a row is added or removed, its corresponding row in the crpmsVpdnGroupCpTable has to be added or removed as well.')
crpmsVpdnGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1), ).setIndexNames((1, "CISCO-RPMS-MIB", "crpmsVpdnGroupName"))
if mibBuilder.loadTexts: crpmsVpdnGroupEntry.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupEntry.setDescription('A VPDN group entry contains information about a specific VPDN group. VPDN groups contain the necessary setting to establish a VPDN session (tunneling protocol, home gateway information, and other data) as well as limits on various parameters (maximum concurrent sessions, MLP bundles, etc.).')
crpmsVpdnGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsVpdnGroupName.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupName.setDescription('The name of the VPDN group. This name uniquely identifies a VPDN group in the RPMS system.')
crpmsVpdnTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnTunnelId.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnTunnelId.setDescription('The tunnel Id of the VPDN group. For Cisco IOS 12.05T and later, the tunnel id matches the remote name configured on the HGW router. The following is an example: vpdn-group 1 accept dialin l2tp virtual-template 1 remote isp1 local name hg For old Cisco IOS releases, the tunnel id matches the incoming statement: vpdn incoming isp1 hgw virtual-template 1 In above examples, the object has the value isp1. ')
crpmsVpdnTunnelProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("l2f", 1), ("l2tp", 2))).clone('l2f')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnTunnelProtocol.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnTunnelProtocol.setDescription('The protocol used by the tunnel of the VPDN group. There are only 2 possible value: l2f - Layer 2 Forwarding Protocol l2tp - Layer 2 Tunneling Protocol ')
crpmsVpdnLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnLimit.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnLimit.setDescription('Limit of the resource pool for this VPDN group.')
crpmsVpdnOverflowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnOverflowLimit.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnOverflowLimit.setDescription('Limit of the overflow pool for this VPDN group.')
crpmsVpdnMlpBundleLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnMlpBundleLimit.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnMlpBundleLimit.setDescription('Limit of MLP (multilink protocol) bundles for this VPDN group.')
crpmsVpdnLinksPerBundleLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnLinksPerBundleLimit.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnLinksPerBundleLimit.setDescription('Limit of links per bundle for this VPDN group.')
crpmsVpdnBundles = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnBundles.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnBundles.setDescription('The number of active MLP bundles in the tunnel of the VPDN group.')
crpmsVpdnActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnActiveCalls.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnActiveCalls.setDescription('The number of active calls that belong to this VPDN group.')
crpmsVpdnActiveOverflowCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnActiveOverflowCalls.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnActiveOverflowCalls.setDescription('The number of active overflow calls that belong to this VPDN group.')
crpmsVpdnRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnRejections.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnRejections.setDescription('The number of calls rejected because one of the group limits (crpmsVpdnOverflowLimit, crpmsVpdnMlpBundleLimit and crpmsVpdnLinksPerBundleLimit) was exceeded.')
crpmsVpdnSizeRejections = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: crpmsVpdnSizeRejections.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnSizeRejections.setDescription('The number of rejected calls of the VPDN group, because the max allowed size limit (crpmsVpdnOverflowLimit + crpmsVpdnLimit) was exceeded.')
crpmsVpdnLimitThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnLimitThreshold.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnLimitThreshold.setDescription('A threshold defined for the vpdn group limit (crpmsVpdnLimit) which, when crossed, triggers a crpmsRisingAlarm or a crpmsFallingAlarm notification (refer to the notification definitions in this MIB for more details). A value of 100 percent cannot be exceeded and therefore disables this threshold setting. A value of 0 percent is always exceeded. ')
crpmsVpdnEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 1, 1, 14), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnEntryStatus.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnEntryStatus.setDescription('Used to create, delete or modify this row. None of the columnar objects can be modified except this one, when the row is active.')
crpmsVpdnGroupCpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2), )
if mibBuilder.loadTexts: crpmsVpdnGroupCpTable.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupCpTable.setDescription("A VPDN group can be associated with a number of customer profiles, this table represents this relationship. It's double indexed by index of crpmsVpdnGroupTable and index of crpmsCpTable. If rows are added to or removed from one of two tables, Its corresponding row(s) in this table will be added or removed as well.")
crpmsVpdnGroupCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-RPMS-MIB", "crpmsVpdnGroupCpVpdnGroupName"), (1, "CISCO-RPMS-MIB", "crpmsVpdnGroupCpCpName"))
if mibBuilder.loadTexts: crpmsVpdnGroupCpEntry.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupCpEntry.setDescription('A VPDN group customer profile entry contains information of SLA associated with this VPDN group.')
crpmsVpdnGroupCpVpdnGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsVpdnGroupCpVpdnGroupName.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupCpVpdnGroupName.setDescription('The name of VPDN groups in the table.')
crpmsVpdnGroupCpCpName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: crpmsVpdnGroupCpCpName.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupCpCpName.setDescription('The name of customer profile in the table.')
crpmsVpdnGroupCpEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: crpmsVpdnGroupCpEntryStatus.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroupCpEntryStatus.setDescription('Used to create, delete or modify this row. None of the columnar objects can be modified except this one, when the row is active.')
crpmsAlarmObject = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crpmsAlarmObject.setStatus('current')
if mibBuilder.loadTexts: crpmsAlarmObject.setDescription('The object identifier of the destination object related to the notification. For example, if crpmsCpLimitThreshold is crossed, this variable should have the OID of crpmsCpLimit.')
crpmsAlarmValue = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crpmsAlarmValue.setStatus('current')
if mibBuilder.loadTexts: crpmsAlarmValue.setDescription('The current value that caused the threshold alarm to be sent.')
crpmsAlarmThresholdObject = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 84, 1, 4, 3), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: crpmsAlarmThresholdObject.setStatus('current')
if mibBuilder.loadTexts: crpmsAlarmThresholdObject.setDescription('The object identifier of the Threshold that is related to the notification. For example, if crpmsCpLimitThreshold is crossed, this variable should have the OID of crpmsCpLimitThreshold.')
ciscoRpmsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 2))
ciscoRpmsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0))
crpmsRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0, 1)).setObjects(("CISCO-RPMS-MIB", "crpmsAlarmObject"), ("CISCO-RPMS-MIB", "crpmsAlarmValue"), ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
if mibBuilder.loadTexts: crpmsRisingAlarm.setStatus('current')
if mibBuilder.loadTexts: crpmsRisingAlarm.setDescription('This trap is generated to notify the manager(s) that one of the thresholds is crossed in rising direction (exceeded). The same trap will not be generated until the sample value falls below the threshold low water mark and rises to cross it again. NOTE: A threshold low water mark is by default 90% of the actual threshold percentage (threshold * 90%) integer rounded. ')
crpmsFallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 84, 2, 0, 2)).setObjects(("CISCO-RPMS-MIB", "crpmsAlarmObject"), ("CISCO-RPMS-MIB", "crpmsAlarmValue"), ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
if mibBuilder.loadTexts: crpmsFallingAlarm.setStatus('current')
if mibBuilder.loadTexts: crpmsFallingAlarm.setDescription('This trap is generated to notify the manager(s) that one of the thresholds is crossed in the falling direction (reaches the threshold low water mark after being exceeded). The same trap will not be generated until the sample value rises above the threshold and reaches the low water mark again. NOTE: A threshold low water mark is by default 90% of the actual threshold percentage (threshold * 90%) integer rounded. ')
ciscoRpmsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 3))
ciscoRpmsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 1))
ciscoRpmsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2))
ciscoRpmsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 1, 1)).setObjects(("CISCO-RPMS-MIB", "crpmsSystemGroup"), ("CISCO-RPMS-MIB", "crpmsCpGroup"), ("CISCO-RPMS-MIB", "crpmsVpdnGroup"), ("CISCO-RPMS-MIB", "crpmsNotifGroup"), ("CISCO-RPMS-MIB", "crpmsThresholdNotifGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsMIBCompliance = ciscoRpmsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoRpmsMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco-RPMS-MIB')
crpmsSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 1)).setObjects(("CISCO-RPMS-MIB", "crpmsSubsystemName"), ("CISCO-RPMS-MIB", "crpmsSubsystemUptime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsSystemGroup = crpmsSystemGroup.setStatus('current')
if mibBuilder.loadTexts: crpmsSystemGroup.setDescription('This group contains a table providing the general system level information.')
crpmsCpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 2)).setObjects(("CISCO-RPMS-MIB", "crpmsCpLimit"), ("CISCO-RPMS-MIB", "crpmsCpOverflowLimit"), ("CISCO-RPMS-MIB", "crpmsCpActiveCalls"), ("CISCO-RPMS-MIB", "crpmsCpActiveOverflowCalls"), ("CISCO-RPMS-MIB", "crpmsCpAttemptedCalls"), ("CISCO-RPMS-MIB", "crpmsCpAttemptedOverflowCalls"), ("CISCO-RPMS-MIB", "crpmsCpRejections"), ("CISCO-RPMS-MIB", "crpmsCpOverflowRejections"), ("CISCO-RPMS-MIB", "crpmsCpLimitThreshold"), ("CISCO-RPMS-MIB", "crpmsCpOverflowLimitThreshold"), ("CISCO-RPMS-MIB", "crpmsCpCallRejectionThreshold"), ("CISCO-RPMS-MIB", "crpmsCpOverflowRejectThreshold"), ("CISCO-RPMS-MIB", "crpmsCpEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsCpGroup = crpmsCpGroup.setStatus('current')
if mibBuilder.loadTexts: crpmsCpGroup.setDescription('This group contains a table providing the information of customer profile.')
crpmsVpdnGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 3)).setObjects(("CISCO-RPMS-MIB", "crpmsVpdnTunnelId"), ("CISCO-RPMS-MIB", "crpmsVpdnTunnelProtocol"), ("CISCO-RPMS-MIB", "crpmsVpdnLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnOverflowLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnMlpBundleLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnLinksPerBundleLimit"), ("CISCO-RPMS-MIB", "crpmsVpdnBundles"), ("CISCO-RPMS-MIB", "crpmsVpdnActiveCalls"), ("CISCO-RPMS-MIB", "crpmsVpdnActiveOverflowCalls"), ("CISCO-RPMS-MIB", "crpmsVpdnRejections"), ("CISCO-RPMS-MIB", "crpmsVpdnSizeRejections"), ("CISCO-RPMS-MIB", "crpmsVpdnLimitThreshold"), ("CISCO-RPMS-MIB", "crpmsVpdnEntryStatus"), ("CISCO-RPMS-MIB", "crpmsVpdnGroupCpEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsVpdnGroup = crpmsVpdnGroup.setStatus('current')
if mibBuilder.loadTexts: crpmsVpdnGroup.setDescription('This group contains tables providing the information of VPDN.')
crpmsNotifGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 4)).setObjects(("CISCO-RPMS-MIB", "crpmsAlarmObject"), ("CISCO-RPMS-MIB", "crpmsAlarmValue"), ("CISCO-RPMS-MIB", "crpmsAlarmThresholdObject"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsNotifGroup = crpmsNotifGroup.setStatus('current')
if mibBuilder.loadTexts: crpmsNotifGroup.setDescription('This group contains helper objects specifying notifications.')
crpmsThresholdNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 84, 3, 2, 5)).setObjects(("CISCO-RPMS-MIB", "crpmsRisingAlarm"), ("CISCO-RPMS-MIB", "crpmsFallingAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    crpmsThresholdNotifGroup = crpmsThresholdNotifGroup.setStatus('current')
if mibBuilder.loadTexts: crpmsThresholdNotifGroup.setDescription('This group contains threshold crossing related alarms and notifications.')
mibBuilder.exportSymbols("CISCO-RPMS-MIB", crpmsCpEntryStatus=crpmsCpEntryStatus, crpmsCpActiveCalls=crpmsCpActiveCalls, crpmsVpdnGroupCpEntry=crpmsVpdnGroupCpEntry, crpmsAlarmValue=crpmsAlarmValue, crpmsCpLimit=crpmsCpLimit, crpmsAlarmObject=crpmsAlarmObject, crpmsVpdnMlpBundleLimit=crpmsVpdnMlpBundleLimit, crpmsCpLimitThreshold=crpmsCpLimitThreshold, crpmsVpdnGroupCpEntryStatus=crpmsVpdnGroupCpEntryStatus, crpmsVpdnGroupCpCpName=crpmsVpdnGroupCpCpName, crpmsVpdnGroupName=crpmsVpdnGroupName, crpmsSubsystemIndex=crpmsSubsystemIndex, crpmsSubsystemName=crpmsSubsystemName, crpmsVpdnRejections=crpmsVpdnRejections, crpmsVpdn=crpmsVpdn, crpmsCpEntry=crpmsCpEntry, PYSNMP_MODULE_ID=ciscoRpmsMIB, crpmsSubsystemUptime=crpmsSubsystemUptime, crpmsVpdnSizeRejections=crpmsVpdnSizeRejections, ciscoRpmsMIBConformance=ciscoRpmsMIBConformance, crpmsSubsystemTable=crpmsSubsystemTable, crpmsFallingAlarm=crpmsFallingAlarm, crpmsVpdnEntryStatus=crpmsVpdnEntryStatus, crpmsRisingAlarm=crpmsRisingAlarm, crpmsCpCallRejectionThreshold=crpmsCpCallRejectionThreshold, crpmsVpdnGroupEntry=crpmsVpdnGroupEntry, crpmsCpAttemptedOverflowCalls=crpmsCpAttemptedOverflowCalls, crpmsCpOverflowRejectThreshold=crpmsCpOverflowRejectThreshold, crpmsVpdnOverflowLimit=crpmsVpdnOverflowLimit, crpmsVpdnGroupCpTable=crpmsVpdnGroupCpTable, ciscoRpmsMIBNotificationPrefix=ciscoRpmsMIBNotificationPrefix, crpmsCustomerProfile=crpmsCustomerProfile, crpmsVpdnLimitThreshold=crpmsVpdnLimitThreshold, crpmsCpOverflowRejections=crpmsCpOverflowRejections, ciscoRpmsMIBObjects=ciscoRpmsMIBObjects, crpmsSubsystemEntry=crpmsSubsystemEntry, crpmsVpdnGroupTable=crpmsVpdnGroupTable, crpmsVpdnGroupCpVpdnGroupName=crpmsVpdnGroupCpVpdnGroupName, crpmsCpAttemptedCalls=crpmsCpAttemptedCalls, crpmsVpdnTunnelId=crpmsVpdnTunnelId, crpmsSystemGroup=crpmsSystemGroup, ciscoRpmsMIBCompliances=ciscoRpmsMIBCompliances, crpmsVpdnActiveOverflowCalls=crpmsVpdnActiveOverflowCalls, crpmsVpdnTunnelProtocol=crpmsVpdnTunnelProtocol, crpmsVpdnBundles=crpmsVpdnBundles, crpmsCpOverflowLimit=crpmsCpOverflowLimit, crpmsSystem=crpmsSystem, crpmsCpGroup=crpmsCpGroup, crpmsNotifGroup=crpmsNotifGroup, crpmsCpRejections=crpmsCpRejections, crpmsCpTable=crpmsCpTable, ciscoRpmsMIBNotifications=ciscoRpmsMIBNotifications, crpmsVpdnGroup=crpmsVpdnGroup, crpmsCpOverflowLimitThreshold=crpmsCpOverflowLimitThreshold, crpmsCpActiveOverflowCalls=crpmsCpActiveOverflowCalls, crpmsAlarmThresholdObject=crpmsAlarmThresholdObject, crpmsVpdnLinksPerBundleLimit=crpmsVpdnLinksPerBundleLimit, ciscoRpmsMIBGroups=ciscoRpmsMIBGroups, ciscoRpmsMIBCompliance=ciscoRpmsMIBCompliance, crpmsThresholdNotifGroup=crpmsThresholdNotifGroup, crpmsNotif=crpmsNotif, ciscoRpmsMIB=ciscoRpmsMIB, crpmsCpName=crpmsCpName, crpmsVpdnActiveCalls=crpmsVpdnActiveCalls, crpmsVpdnLimit=crpmsVpdnLimit)
