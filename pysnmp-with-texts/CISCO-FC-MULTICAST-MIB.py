#
# PySNMP MIB module CISCO-FC-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FC-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
DomainIdOrZero, = mibBuilder.importSymbols("CISCO-ST-TC", "DomainIdOrZero")
vsanIndex, = mibBuilder.importSymbols("CISCO-VSAN-MIB", "vsanIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Integer32, Counter64, IpAddress, MibIdentifier, NotificationType, Gauge32, Bits, iso, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Integer32", "Counter64", "IpAddress", "MibIdentifier", "NotificationType", "Gauge32", "Bits", "iso", "ObjectIdentity", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoFcMulticastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 435))
ciscoFcMulticastMIB.setRevisions(('2004-10-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFcMulticastMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setLastUpdated('200410070000Z')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setOrganization('Cisco Systems Inc. ')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoFcMulticastMIB.setDescription('MIB module for monitoring and configuring Fibre Channel Multicast feature.')
ciscoFcMulticastNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 0))
ciscoFcMulticastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1))
ciscoFcMulticaseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2))
cfmConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1))
class CfmMulticastRootMode(TextualConvention, Integer32):
    reference = 'Refer to FC-SW-2 REV 5.4 for information on principal switch and lowest domain id switch.'
    description = 'The multicast Root Mode. principalSwitch - principal switch is used as the root for multicast tree computation. lowestDomainIdSwitch - lowest domainId switch is used as the root for mulitcast tree computation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("principalSwitch", 1), ("lowestDomainSwitch", 2))

cfmMulticastRootTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1), )
if mibBuilder.loadTexts: cfmMulticastRootTable.setReference('For information FC multicast/root, refer to Fibre Channel Switch Fabric-2 (FC-SW-2 REV 5.4) and Fibre Channel Switch Fabric-3 (FC-SW-3 REV 6.6).')
if mibBuilder.loadTexts: cfmMulticastRootTable.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootTable.setDescription("This table allows the users to configure and monitor the FC Multicast parameters on all the VSANs configured on the local switch. An entry is automatically created in this table if there is an entry in the fspfTable (defined in CISCO-FSPF-MIB) and fspfOperStatus (defined in CISCO-FSPF-MIB) for that entry is 'up'. An entry is automatically deleted from this table if either : a) the fspfOperStatus in the fspfTable entry for the corresponding VSAN changes to 'down'. or b) the fspfTable entry for the corresponding VSAN is deleted. Entries in this table can be created via cfmMulticastRootRowStatus only as the means to specify non-default parameter values for a VSAN either because the VSAN is suspended or fspfOperStatus (defined in CISCO-FSPF-MIB) for that VSAN is 'down' (VSAN state is indicated by object vsanOperState which is defined in CISCO-VSAN-MIB). So an entry in this table exists when one or both of these conditions holds: - one or more configuration parameters have non-default values for a VSAN which is either suspended or the fspfOperStatus for that VSAN is down. - the fspfOperStatus for VSAN is 'up'. This has a number of consequences: - an entry exists for a suspended VSAN whenever that VSAN has non-default parameters. - an entry cannot be created (via cfmMulticastRootRowStatus) for a VSAN with default parameters; instead, the agent creates/deletes an entry for a VSAN with default parameters according to whether the fspfOperStatus is 'up' or 'down'. - an entry can not be created via cfmMulticastRootRowStatus unless non-default parameter values are (simultaneously) configured for a VSAN whose fspfOperStatus is 'down'. - deleting an entry via cfmMulticastRootRowStatus when either the VSAN is suspended and configured with non-default values or the VSAN is active, is equivalent to resetting its parameters to their default values. If an entry is configured with default-values and the VSAN is in suspended state, then the entry would be deleted.")
cfmMulticastRootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VSAN-MIB", "vsanIndex"))
if mibBuilder.loadTexts: cfmMulticastRootEntry.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootEntry.setDescription('This entry contains the multicase parameters on this VSAN.')
cfmMulticastRootConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 1), CfmMulticastRootMode().clone('principalSwitch')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootConfigMode.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootConfigMode.setDescription('The configured multicast root mode on this VSAN.')
cfmMulticastRootOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 2), CfmMulticastRootMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootOperMode.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootOperMode.setDescription('The operational multicast root mode on this VSAN.')
cfmMulticastRootDomainId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 3), DomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmMulticastRootDomainId.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootDomainId.setDescription('The domainID of the multicast root on this VSAN.')
cfmMulticastRootRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 435, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmMulticastRootRowStatus.setStatus('current')
if mibBuilder.loadTexts: cfmMulticastRootRowStatus.setDescription('The status of conceptual row on this VSAN. This object can be used to create an entry only if either the corresponding VSAN is suspended or the fspfOperStatus is down. If the VSAN is either not-existent or fspfOperStatus is up, the create will fail.')
ciscoFcMulticastMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1))
ciscoFcMulticastMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2))
ciscoFcMulticastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 1, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFcMulticastMIBCompliance = ciscoFcMulticastMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoFcMulticastMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-FC-MULTICAST-MIB.')
cfmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 435, 2, 2, 1)).setObjects(("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootConfigMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootOperMode"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootDomainId"), ("CISCO-FC-MULTICAST-MIB", "cfmMulticastRootRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmConfigurationGroup = cfmConfigurationGroup.setStatus('current')
if mibBuilder.loadTexts: cfmConfigurationGroup.setDescription('A collection of objects for FC multicast configuration.')
mibBuilder.exportSymbols("CISCO-FC-MULTICAST-MIB", PYSNMP_MODULE_ID=ciscoFcMulticastMIB, cfmConfigurationGroup=cfmConfigurationGroup, cfmMulticastRootDomainId=cfmMulticastRootDomainId, ciscoFcMulticastNotifications=ciscoFcMulticastNotifications, cfmMulticastRootConfigMode=cfmMulticastRootConfigMode, ciscoFcMulticaseConformance=ciscoFcMulticaseConformance, CfmMulticastRootMode=CfmMulticastRootMode, ciscoFcMulticastMIBObjects=ciscoFcMulticastMIBObjects, cfmMulticastRootOperMode=cfmMulticastRootOperMode, cfmMulticastRootEntry=cfmMulticastRootEntry, cfmMulticastRootRowStatus=cfmMulticastRootRowStatus, ciscoFcMulticastMIBCompliances=ciscoFcMulticastMIBCompliances, ciscoFcMulticastMIBCompliance=ciscoFcMulticastMIBCompliance, cfmMulticastRootTable=cfmMulticastRootTable, ciscoFcMulticastMIBGroups=ciscoFcMulticastMIBGroups, ciscoFcMulticastMIB=ciscoFcMulticastMIB, cfmConfiguration=cfmConfiguration)
