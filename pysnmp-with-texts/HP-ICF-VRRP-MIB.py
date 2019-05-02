#
# PySNMP MIB module HP-ICF-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-VRRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, NotificationType, IpAddress, ModuleIdentity, TimeTicks, Counter32, Unsigned32, Gauge32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "NotificationType", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter32", "Unsigned32", "Gauge32", "ObjectIdentity", "iso")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
vrrpAssoIpAddrEntry, vrrpOperVrId, vrrpOperEntry = mibBuilder.importSymbols("VRRP-MIB", "vrrpAssoIpAddrEntry", "vrrpOperVrId", "vrrpOperEntry")
hpicfVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31))
hpicfVrrpMIB.setRevisions(('2012-11-15 00:00', '2013-06-12 00:00', '2012-02-22 00:00', '2010-10-20 00:00', '2010-07-28 00:00', '2009-05-19 00:00', '2008-02-20 00:00', '2007-12-12 00:00', '2007-08-22 00:00', '2005-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfVrrpMIB.setRevisionsDescriptions(('Deprecate mib objects hpicfVrrpRespondToPing, hpicfVrrpRemoveConfig, hpicfVrrpStatsNearFailovers, hpicfVrrpNonstop, hpicfVrrpAdminStatus', 'Deprecate mib objects hpicfVrrpAdminStatus, hpicfVrrpRespondToPing, hpicfVrrpRemoveConfig, hpicfVrrpNonstop.Deprecated groups hpicfVrrpOperGroup,hpicfVrrpOperationsGroup and added hpicfVrrpOperGroup1, hpicfVrrpOperationsGroup. Deprecated compliances hpicfVrrpMIBCompliance3, hpicfVrrpMIBCompliance4,hpicfVrrpMIBCompliance5 and added hpicfVrrpMIBCompliance6 and hpicfVrrpMIBCompliance7. ', 'Added hpicfVrrpTrackState, hpicfVrrpTrackGroup1 and hpicfVrrpMIBCompliance5.deprecated hpicfVrrpMIBCompliance1.', 'Added hpicfVrrpNonstop to the hpicfVrrpOperations object', 'Added hpicfVrrpRemoveConfig to disable VRRP and remove its entire config schema from the switch. hpicfVrrpRemoveConfig to the hpicfVrrpOperations object', 'Added hpicfVrrpRespondToPing to enable/disable response to ping in the global context and added hpicfVrrpVrRespondToPing to the hpicfVrrpOperEntry object', 'Added hpicfVrrpVrControl, to the hpicfVrrpOperEntry object. Added hpicfVrrpTrackTable containing hpicfVrrpTrackEntry to hpicfVrrpOperations.', 'Added hpicfVrrpStatsTable, which contains hpicfVrrpStatsNearFailovers.', 'Added hpicfVrrpVrPreemptDelayTime to the hpicfVrrpOperEntry object.', 'Initial revision.',))
if mibBuilder.loadTexts: hpicfVrrpMIB.setLastUpdated('201211150000Z')
if mibBuilder.loadTexts: hpicfVrrpMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfVrrpMIB.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfVrrpMIB.setDescription('This MIB module contains HP proprietary extensions to the standard VRRP MIB (RFC 2787).')
hpicfVrrpOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1))
hpicfVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2))
hpicfVrrpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpAdminStatus.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpAdminStatus.setDescription('When set to TRUE, this enables VRRP ipv4 globally on the router. If set to FALSE, this would disable VRRP. Default is FALSE. This mib Object is deprecated and alternate mib object is hpicfVrrpv3IPv4AdminStatus.')
hpicfVrrpOperTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2), )
if mibBuilder.loadTexts: hpicfVrrpOperTable.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpOperTable.setDescription('HP extensions to the vrrpOperTable (RFC 2787).')
hpicfVrrpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1), )
vrrpOperEntry.registerAugmentions(("HP-ICF-VRRP-MIB", "hpicfVrrpOperEntry"))
hpicfVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVrrpOperEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpOperEntry.setDescription('HP extensions for an entry in the vrrpOperTable.')
hpicfVrrpVrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("owner", 1), ("backup", 2), ("uninitialized", 3))).clone('uninitialized')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrMode.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrMode.setDescription('This object denotes whether this VR has been designated as an owner or as a backup. On VR creation, this field is set to uninitialized. The user cannot set the value of this object to uninitialized.')
hpicfVrrpVrMasterPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrMasterPreempt.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrMasterPreempt.setDescription('This object, when set to TRUE, would enable the Master Preemption mode wherein a virtual router even though an owner will not preempt a lower priority Backup.')
hpicfVrrpVrTransferControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrTransferControl.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrTransferControl.setDescription('This object, when set to TRUE, would serve as trigger to enable a virtual router owner to take control of its IP address. When this value is read it always returns FALSE.')
hpicfVrrpVrPreemptDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrPreemptDelayTime.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrPreemptDelayTime.setDescription('This object specifies the time that the owner virtual router will wait before taking control of its virtual IP address. A value of 0 indicates that the pre-empt delay timer is not active')
hpicfVrrpVrControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("failback", 1), ("failover", 2), ("failoverWithMonitoring", 3), ("invalid", 4))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrControl.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrControl.setDescription('When this object is set to failback (1), it acts as a trigger to intimate VRRP to failback to this router from another. When this object is set to failover (2), it acts as a trigger to intimate VRRP to failover from this router to another. When this object is set to failoverWithMonitoring (3), in addition to triggering VRRP to failover, it triggers VR to monitor for presence of a master. When read, this object always returns invalid (4).')
hpicfVrrpVrRespondToPing = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 2, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpVrRespondToPing.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrRespondToPing.setDescription('If set to FALSE, prevents a response to ping requests to the virtual router IP addresses configured on the backup router. If set to TRUE allows response to ping requests to virtual IP addresses configured when virtual router become master. hpicfVrrpRespondToPing must also be configured globally to respond to virtual IP ping requests. By default hpicfVrrpVrRespondToPing is enabled.')
hpicfVrrpAssoIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3), )
if mibBuilder.loadTexts: hpicfVrrpAssoIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpAssoIpAddrTable.setDescription('HP extensions to the vrrpAssoIpAddrTable (RFC 2787).')
hpicfVrrpAssoIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3, 1), )
vrrpAssoIpAddrEntry.registerAugmentions(("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpAddrEntry"))
hpicfVrrpAssoIpAddrEntry.setIndexNames(*vrrpAssoIpAddrEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVrrpAssoIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpAssoIpAddrEntry.setDescription('HP extensions for an entry in the vrrpAssoIpAddrTable.')
hpicfVrrpAssoIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 3, 1, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpAssoIpMask.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpAssoIpMask.setDescription("The subnet mask to be used in conjunction with the 'vrrpAssoIpAddr' object to uniquely identify a subnet.")
hpicfVrrpTrackTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5), )
if mibBuilder.loadTexts: hpicfVrrpTrackTable.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpTrackTable.setDescription('HP extensions for supporting tracking.')
hpicfVrrpTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "HP-ICF-VRRP-MIB", "hpicfVrrpVrTrackType"), (0, "HP-ICF-VRRP-MIB", "hpicfVrrpVrTrackEntity"))
if mibBuilder.loadTexts: hpicfVrrpTrackEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpTrackEntry.setDescription('HP extensions for supporting tracking.')
hpicfVrrpVrTrackType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("port", 1), ("trunk", 2), ("vlan", 3))))
if mibBuilder.loadTexts: hpicfVrrpVrTrackType.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrTrackType.setDescription("This object specifies the type of interface specified by 'hpicfVrrpVrTrackEntity'.")
hpicfVrrpVrTrackEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: hpicfVrrpVrTrackEntity.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrTrackEntity.setDescription("This object specifies interface details. Interface detail is interpreted Based on type specified by 'hpicfVrrpVrTrackType'. Valid values for different track types are - ------------------------------------ hpicfVrrpVrTrackType range ------------------------------------ port '1'..'65535' trunk '1'..'65535' vlan '1'..'65535' ------------------------------------")
hpicfVrrpTrackRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfVrrpTrackRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpTrackRowStatus.setDescription('The row status of given track entity.')
hpicfVrrpTrackState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("down", 0), ("up", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVrrpTrackState.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpTrackState.setDescription('This object specifies the state of the Vrrp track.')
hpicfVrrpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6), )
if mibBuilder.loadTexts: hpicfVrrpStatsTable.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpStatsTable.setDescription('Table of virtual router statistics.')
hpicfVrrpRespondToPing = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpRespondToPing.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpRespondToPing.setDescription('If this object is set to FALSE globally, it prevents a response to ping requests to the virtual router IP addresses configured on all backup routers.If set to TRUE, allows response to ping requests to virtual IP addresses configured on backup virtual routers when they become master. hpicfVrrpVrRespondToPing object must also be configured on a Virtual router to respond to virtual IP ping requests. By default hpicfVrrpRespondToPing is disabled. This MIB object is deprecated and the alternate MIB object is hpicfVrrpv3RespondToPing.')
hpicfVrrpRemoveConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpRemoveConfig.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpRemoveConfig.setDescription("This objects clears all existing vrrp configuration and again intializes it with default values when this is set with value 'true'. It also clears (disables) the global VRRP enable flag. SnmpGet on this will always return false. This MIB object is deprecated and the alternate MIB object is hpicfVrrpv3RemoveConfig.")
hpicfVrrpNonstop = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 9), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfVrrpNonstop.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpNonstop.setDescription('This object defines the operation of VRRP on redundant platforms. When set to TRUE, the VRRP Master router will retain control of virtual-IP addresses across a management card failure on redundant platforms. When set to FALSE, the VRRP Backup router will take control of virtual-IP addresses on the network on the occurrence of a management card failure on the Master VRRP router. This MIB object is deprecated and the alternate MIB object is hpicfVrrpv3Nonstop.')
hpicfVrrpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6, 1), )
vrrpOperEntry.registerAugmentions(("HP-ICF-VRRP-MIB", "hpicfVrrpStatsEntry"))
hpicfVrrpStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfVrrpStatsEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpStatsEntry.setDescription('An entry in the table, containing statistics information about a given virtual router.')
hpicfVrrpStatsNearFailovers = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfVrrpStatsNearFailovers.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpStatsNearFailovers.setDescription('This object reports the number of near failovers for backup virtual routers. A near failover occurs when a backup virtual router has not received an advertisement packet from the master virtual router for two advertisement intervals.')
hpicfVrrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1))
hpicfVrrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2))
hpicfVrrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 1)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance = hpicfVrrpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance.setDescription('The compliance statement for HP routers running VRRP (RFC 3768) and implementing the HP-ICF-VRRP-MIB.')
hpicfVrrpMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 2)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance1 = hpicfVrrpMIBCompliance1.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance1.setDescription('The compliance statement for HP routers running VRRP (RFC 3768) and implementing the HP-ICF-VRRP-MIB.')
hpicfVrrpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 3)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrPingGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance2 = hpicfVrrpMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance2.setDescription('Support for this group is required for HP backup routers to respond to ping request.')
hpicfVrrpMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 4)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpNonstopGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpNonstopGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance3 = hpicfVrrpMIBCompliance3.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance3.setDescription('Support for this group is required for HP routers that supports non-stop vrrp.')
hpicfVrrpMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 5)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance4 = hpicfVrrpMIBCompliance4.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance4.setDescription('Support for this group is required for HP routers that supports non-stop vrrp.')
hpicfVrrpMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 6)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance5 = hpicfVrrpMIBCompliance5.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance5.setDescription('The compliance statement for HP routers running VRRP (RFC 3768) and implementing the HP-ICF-VRRP-MIB.')
hpicfVrrpMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 7)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpOperGroup1"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance6 = hpicfVrrpMIBCompliance6.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance6.setDescription('The compliance statement for HP routers running VRRP (RFC 3768) and implementing the HP-ICF-VRRP-MIB.')
hpicfVrrpMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 1, 8)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpOperationsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpMIBCompliance7 = hpicfVrrpMIBCompliance7.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpMIBCompliance7.setDescription('Support for this group is required for HP routers that supports non-stop vrrp.')
hpicfVrrpOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 1)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpAdminStatus"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"), ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperGroup = hpicfVrrpOperGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpOperGroup.setDescription('A collection of HP proprietary objects to support VRRP configuration on HP routers.')
hpicfVrrpTrackGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 2)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpTrackRowStatus"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpTrackGroup = hpicfVrrpTrackGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpTrackGroup.setDescription('A collection of HP proprietary objects to support VRRP configuration on HP routers.')
hpicfVrrpVrPingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 3)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrRespondToPing"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpVrPingGroup = hpicfVrrpVrPingGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpVrPingGroup.setDescription('A HP proprietary object to support VRRP Virtual IP Ping on a backup router.')
hpicfVrrpNonstopGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 4)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpNonstop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpNonstopGroup = hpicfVrrpNonstopGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpNonstopGroup.setDescription('A HP proprietary object to support nonstop VRRP on HP routers.')
hpicfVrrpOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 5)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpRespondToPing"), ("HP-ICF-VRRP-MIB", "hpicfVrrpRemoveConfig"), ("HP-ICF-VRRP-MIB", "hpicfVrrpStatsNearFailovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperationsGroup = hpicfVrrpOperationsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: hpicfVrrpOperationsGroup.setDescription('A HP proprietary object to support nonstop VRRP on HP routers.')
hpicfVrrpTrackGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 6)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpTrackRowStatus"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpTrackState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpTrackGroup1 = hpicfVrrpTrackGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpTrackGroup1.setDescription('A collection of HP proprietary objects to support VRRP configuration on HP routers.')
hpicfVrrpOperGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 7)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpVrMode"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrMasterPreempt"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrTransferControl"), ("HP-ICF-VRRP-MIB", "hpicfVrrpVrPreemptDelayTime"), ("HP-ICF-VRRP-MIB", "hpicfVrrpAssoIpMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperGroup1 = hpicfVrrpOperGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpOperGroup1.setDescription('A collection of HP proprietary objects to support VRRP configuration on HP routers.')
hpicfVrrpOperationsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31, 2, 2, 8)).setObjects(("HP-ICF-VRRP-MIB", "hpicfVrrpStatsNearFailovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfVrrpOperationsGroup1 = hpicfVrrpOperationsGroup1.setStatus('current')
if mibBuilder.loadTexts: hpicfVrrpOperationsGroup1.setDescription('A HP proprietary object to support nonstop VRRP on HP routers.')
mibBuilder.exportSymbols("HP-ICF-VRRP-MIB", hpicfVrrpMIBCompliances=hpicfVrrpMIBCompliances, hpicfVrrpMIBCompliance7=hpicfVrrpMIBCompliance7, hpicfVrrpConformance=hpicfVrrpConformance, hpicfVrrpVrRespondToPing=hpicfVrrpVrRespondToPing, hpicfVrrpMIBCompliance5=hpicfVrrpMIBCompliance5, hpicfVrrpVrControl=hpicfVrrpVrControl, hpicfVrrpTrackState=hpicfVrrpTrackState, hpicfVrrpAssoIpAddrTable=hpicfVrrpAssoIpAddrTable, hpicfVrrpAssoIpMask=hpicfVrrpAssoIpMask, hpicfVrrpTrackEntry=hpicfVrrpTrackEntry, hpicfVrrpNonstop=hpicfVrrpNonstop, hpicfVrrpStatsEntry=hpicfVrrpStatsEntry, hpicfVrrpOperGroup1=hpicfVrrpOperGroup1, hpicfVrrpTrackRowStatus=hpicfVrrpTrackRowStatus, hpicfVrrpVrMasterPreempt=hpicfVrrpVrMasterPreempt, hpicfVrrpOperTable=hpicfVrrpOperTable, hpicfVrrpVrPreemptDelayTime=hpicfVrrpVrPreemptDelayTime, hpicfVrrpVrTrackEntity=hpicfVrrpVrTrackEntity, hpicfVrrpOperGroup=hpicfVrrpOperGroup, hpicfVrrpVrTrackType=hpicfVrrpVrTrackType, hpicfVrrpVrPingGroup=hpicfVrrpVrPingGroup, hpicfVrrpOperationsGroup=hpicfVrrpOperationsGroup, hpicfVrrpMIBCompliance3=hpicfVrrpMIBCompliance3, hpicfVrrpTrackTable=hpicfVrrpTrackTable, hpicfVrrpAssoIpAddrEntry=hpicfVrrpAssoIpAddrEntry, PYSNMP_MODULE_ID=hpicfVrrpMIB, hpicfVrrpVrMode=hpicfVrrpVrMode, hpicfVrrpTrackGroup1=hpicfVrrpTrackGroup1, hpicfVrrpMIBCompliance1=hpicfVrrpMIBCompliance1, hpicfVrrpRespondToPing=hpicfVrrpRespondToPing, hpicfVrrpStatsTable=hpicfVrrpStatsTable, hpicfVrrpMIB=hpicfVrrpMIB, hpicfVrrpTrackGroup=hpicfVrrpTrackGroup, hpicfVrrpMIBCompliance4=hpicfVrrpMIBCompliance4, hpicfVrrpOperationsGroup1=hpicfVrrpOperationsGroup1, hpicfVrrpMIBGroups=hpicfVrrpMIBGroups, hpicfVrrpMIBCompliance6=hpicfVrrpMIBCompliance6, hpicfVrrpOperEntry=hpicfVrrpOperEntry, hpicfVrrpVrTransferControl=hpicfVrrpVrTransferControl, hpicfVrrpMIBCompliance2=hpicfVrrpMIBCompliance2, hpicfVrrpRemoveConfig=hpicfVrrpRemoveConfig, hpicfVrrpMIBCompliance=hpicfVrrpMIBCompliance, hpicfVrrpNonstopGroup=hpicfVrrpNonstopGroup, hpicfVrrpStatsNearFailovers=hpicfVrrpStatsNearFailovers, hpicfVrrpOperations=hpicfVrrpOperations, hpicfVrrpAdminStatus=hpicfVrrpAdminStatus)
