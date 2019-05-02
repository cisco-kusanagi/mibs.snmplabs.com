#
# PySNMP MIB module CISCO-SLB-DFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SLB-DFP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:12:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
EntPhysicalIndexOrZero, = mibBuilder.importSymbols("CISCO-TC", "EntPhysicalIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Bits, ModuleIdentity, IpAddress, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, ObjectIdentity, MibIdentifier, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSlbDfpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 689))
ciscoSlbDfpMIB.setRevisions(('2009-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbDfpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setLastUpdated('200901290000Z')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setContactInfo('Cisco Systems Customer Service Postal:170 W. Tasman Drive San Jose, CA 95134 USA Tel:+1 800 553-NETS E-mail:cs-asngw@cisco.com')
if mibBuilder.loadTexts: ciscoSlbDfpMIB.setDescription('This MIB reports the congestion status of the real server. A server can be in congested state due to high memory consumption, high CPU utilization or high number of clients being served by it. Congestion can cause delay in server response time. DFP (Dynamic Feedback Protocol) weight values are used as a metric to monitor the congestion of the server. This MIB generates notifications when congestion state is detected on the real server. DFP weight is calculated as follows BindingWeight=(Maxbindings-numberOfBindings)/Maxbindings CPUMemWeight=(cpu + mem)/32 Weight = BindingWeight*CPUMemWeight*dfp_max_weight Here, - Maxbindings is the maximum number of bindings allowed on the server. - dfp_max_weight is the maximum possible value of DFP weight (24). - numberOfBindings is the number of mobile bindings currently present with the server. The DFP weight at which congestion is detected is configurable. If the DFP weight of the system falls below this value, then the system is treated as congested and notification is generated.')
ciscoSlbDfpMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 0))
ciscoSlbDfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 1))
ciscoSlbDfpMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2))
cslbcDfpCongestionThresholdType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("reject", 1), ("abort", 2), ("redirect", 3), ("drop", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cslbcDfpCongestionThresholdType.setStatus('current')
if mibBuilder.loadTexts: cslbcDfpCongestionThresholdType.setDescription('This object specifies the action taken when the congestion threshold is reached. The valid congestion action type are o reject - Incoming registration requests will be rejected when this congestion type is configured. o abort - Registration request being processed will be aborted when this congestion type is configured. o redirect - Incoming registration requests will be redirected to another Home Agent when this congestion type is configured. o drop - Existing idle mobile IP bindings will be dropped when this congestion type is configured. A mobile IP binding is a record present with the server that associates the home address given to the mobile node by its home network with the care of address granted to it by the foreign network while it is roaming. The Home Agent is a real server that maintains mobile bindings.')
cslbcProcessorDfpValTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4), )
if mibBuilder.loadTexts: cslbcProcessorDfpValTable.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValTable.setDescription('This table lists the DFP status for each processor for which DFP weights are monitored.')
cslbcProcessorDfpValEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1), ).setIndexNames((0, "CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValPhysicalIndex"))
if mibBuilder.loadTexts: cslbcProcessorDfpValEntry.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValEntry.setDescription('The entry contains DFP value for one processor. A row is added to this table when congestion needs to be monitored on a processor. Row is deleted when congestion no longer needs to be monitored.')
cslbcProcessorDfpValPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 1), EntPhysicalIndexOrZero())
if mibBuilder.loadTexts: cslbcProcessorDfpValPhysicalIndex.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValPhysicalIndex.setDescription('This element contains the index of the physical entity or identifier of the processor for which the DFP value is maintained.')
cslbcProcessorDfpValDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDescription.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValDescription.setDescription('This element contains the description for the congestion configured on for processor.')
class CslbcDfpValue(TextualConvention, Unsigned32):
    description = 'This textual convention defines valid ranges DFP values similar to slbDfpRealWeight object defined in CISCO-SLB-MIB.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

cslbcDfpCongestionOnsetThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 1), CslbcDfpValue()).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionOnsetThreshold.setStatus('current')
if mibBuilder.loadTexts: cslbcDfpCongestionOnsetThreshold.setDescription('This object specifes when congestion occurs. When the DFP level of the system drops below this value, the system is marked as congested. This value is same for all the processors.')
cslbcDfpCongestionAbateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 2), CslbcDfpValue()).setUnits('DFP weight').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cslbcDfpCongestionAbateThreshold.setStatus('current')
if mibBuilder.loadTexts: cslbcDfpCongestionAbateThreshold.setDescription('This object specifies when decongestion occurs. When the DFP level of the system rises above this value, the system is marked as decongested. This value is same for all processors.')
cslbcProcessorDfpValDfpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 689, 1, 4, 1, 3), CslbcDfpValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cslbcProcessorDfpValDfpValue.setStatus('current')
if mibBuilder.loadTexts: cslbcProcessorDfpValDfpValue.setDescription('This object indicates DFP value for the processor.')
cslbcSlbDfpCongestionOnset = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionOnset.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpCongestionOnset.setDescription('The server generates this notification when value of cslbcInstanceDfpValue object drops below the threshold indicated by the cslbcDfpCongestionOnsetThreshold object.')
cslbcSlbDfpCongestionAbate = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 689, 0, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if mibBuilder.loadTexts: cslbcSlbDfpCongestionAbate.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpCongestionAbate.setDescription('The server generates this notification when value of cslbcInstanceDfpValue object rises above the threshold indicated by the cslbcDfpCongestionAbateThreshold object.')
ciscoSlbDfpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1))
ciscoSlbDfpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2))
ciscoSlbDfpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 1, 1)).setObjects(("CISCO-SLB-DFP-MIB", "ciscoSlbDfpInstanceGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpScalarsGroup"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpMIBCompliance = ciscoSlbDfpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbDfpMIBCompliance.setDescription('The compliance statement for entities which implement ciscoSlbDfp MIB module.')
ciscoSlbDfpInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 1)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDescription"), ("CISCO-SLB-DFP-MIB", "cslbcProcessorDfpValDfpValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbDfpInstanceGroup = ciscoSlbDfpInstanceGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbDfpInstanceGroup.setDescription('This group represents the fields that identifies the processor and associated DFP value.')
cslbcSlbDfpScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 2)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionOnsetThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionAbateThreshold"), ("CISCO-SLB-DFP-MIB", "cslbcDfpCongestionThresholdType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpScalarsGroup = cslbcSlbDfpScalarsGroup.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpScalarsGroup.setDescription('This group represents the set of thresholds against which the DFP value is compared.')
cslbcSlbDfpCongestionGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 689, 2, 2, 3)).setObjects(("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionOnset"), ("CISCO-SLB-DFP-MIB", "cslbcSlbDfpCongestionAbate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cslbcSlbDfpCongestionGroup = cslbcSlbDfpCongestionGroup.setStatus('current')
if mibBuilder.loadTexts: cslbcSlbDfpCongestionGroup.setDescription('This groutp represents the group of notifications on Home Agent.')
mibBuilder.exportSymbols("CISCO-SLB-DFP-MIB", cslbcProcessorDfpValDfpValue=cslbcProcessorDfpValDfpValue, PYSNMP_MODULE_ID=ciscoSlbDfpMIB, cslbcSlbDfpScalarsGroup=cslbcSlbDfpScalarsGroup, cslbcProcessorDfpValPhysicalIndex=cslbcProcessorDfpValPhysicalIndex, cslbcSlbDfpCongestionOnset=cslbcSlbDfpCongestionOnset, ciscoSlbDfpMIBCompliances=ciscoSlbDfpMIBCompliances, ciscoSlbDfpMIBObjects=ciscoSlbDfpMIBObjects, CslbcDfpValue=CslbcDfpValue, cslbcProcessorDfpValTable=cslbcProcessorDfpValTable, cslbcSlbDfpCongestionGroup=cslbcSlbDfpCongestionGroup, ciscoSlbDfpMIBNotifs=ciscoSlbDfpMIBNotifs, cslbcProcessorDfpValDescription=cslbcProcessorDfpValDescription, cslbcDfpCongestionOnsetThreshold=cslbcDfpCongestionOnsetThreshold, cslbcDfpCongestionAbateThreshold=cslbcDfpCongestionAbateThreshold, ciscoSlbDfpMIBGroups=ciscoSlbDfpMIBGroups, ciscoSlbDfpMIBConform=ciscoSlbDfpMIBConform, cslbcDfpCongestionThresholdType=cslbcDfpCongestionThresholdType, ciscoSlbDfpInstanceGroup=ciscoSlbDfpInstanceGroup, cslbcSlbDfpCongestionAbate=cslbcSlbDfpCongestionAbate, ciscoSlbDfpMIB=ciscoSlbDfpMIB, cslbcProcessorDfpValEntry=cslbcProcessorDfpValEntry, ciscoSlbDfpMIBCompliance=ciscoSlbDfpMIBCompliance)
