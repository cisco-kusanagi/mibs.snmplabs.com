#
# PySNMP MIB module JUNIPER-SP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:58:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, Counter32, Counter64, IpAddress, MibIdentifier, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "Counter64", "IpAddress", "MibIdentifier", "Bits", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxSpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 32))
jnxSpMIB.setRevisions(('2005-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxSpMIB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: jnxSpMIB.setLastUpdated('200504050000Z')
if mibBuilder.loadTexts: jnxSpMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxSpMIB.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxSpMIB.setDescription('Provides data about each of the AS Pics on a router.')
jnxSpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0))
jnxFlowLimitTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 32, 2))
jnxSpSvcSet = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1))
if mibBuilder.loadTexts: jnxSpSvcSet.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSet.setDescription('Information about Service PIC Service Sets.')
jnxSpSvcSetTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1), )
if mibBuilder.loadTexts: jnxSpSvcSetTable.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetTable.setDescription('Data about each service set on each Service PIC on the router.')
jnxSpSvcSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1), ).setIndexNames((0, "JUNIPER-SP-MIB", "jnxSpSvcSetName"))
if mibBuilder.loadTexts: jnxSpSvcSetEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetEntry.setDescription('Each entry provides information about a single Service Set. The Service Set is identified by its name and the Service PIC the Service Set is configured on is identified by jnxSpSvcSetIfName.')
jnxSpSvcSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 96)))
if mibBuilder.loadTexts: jnxSpSvcSetName.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetName.setDescription('The Service Set name.')
jnxSpSvcSetSvcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcType.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcType.setDescription('The name of the Service Type associated with this table entry.')
jnxSpSvcSetTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetTypeIndex.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetTypeIndex.setDescription('A generic integer used to identify the Service Type for this entry.')
jnxSpSvcSetIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfName.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfName.setDescription('The ifName of the interface identifying the Service PIC. If more than one interface is associated with the Service PIC, the name associated with the lowest layer interface is used for this object.')
jnxSpSvcSetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfIndex.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfIndex.setDescription('The ifIndex corresponding to jnxSpSvcSetIfName.')
jnxSpSvcSetMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 6), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetMemoryUsage.setDescription('The amount of memory used by this Service Set, expressed in bytes.')
jnxSpSvcSetCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 7), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetCpuUtil.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetCpuUtil.setDescription('The amount of CPU used by this Service Set, expressed as a percentage of the total.')
jnxSpSvcSetSvcStyle = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("interface-service", 2), ("next-hop-service", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcStyle.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcStyle.setDescription('The type of this Service Set. The definitions of each style being: Unknown - Service style is not known. Interface-service - Service style is interface based. Next-hop-service - Service style is next-hop based.')
jnxSpSvcSetMemLimitPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetMemLimitPktDrops.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetMemLimitPktDrops.setDescription('The number of packets dropped due to the Service Set exceeding its memory limits (when in Red Zone).')
jnxSpSvcSetCpuLimitPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetCpuLimitPktDrops.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetCpuLimitPktDrops.setDescription('The number of packets dropped due to the Service Set exceeding the average cpu limits (when total exceeds 85%).')
jnxSpSvcSetFlowLimitPktDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitPktDrops.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitPktDrops.setDescription('The number of packets dropped due to the Service Set exceeding the flow limit.')
jnxSpSvcSetSvcTypeTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2), )
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeTable.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeTable.setDescription('Data about each service on each Service PIC on the router.')
jnxSpSvcSetSvcTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-SP-MIB", "jnxSpSvcSetSvcTypeIndex"))
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeEntry.setDescription('Each entry provides information about a single Service on each Service PIC. Each Service PIC is identified by its corresponding ifIndex, while each Service is identified by jnxSpSvcSetSvcTypeIndex. The Service Type associated with this index is provided by jnxSpSvcSetSvcTypeName.')
jnxSpSvcSetSvcTypeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeIndex.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeIndex.setDescription('A generic integer used to identify the Service Type for this entry.')
jnxSpSvcSetSvcTypeIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeIfName.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeIfName.setDescription('The ifName of the interface identifying the Service PIC. If more than one interface is associated with the Service PIC, the name associated with the lowest layer interface is used for this object.')
jnxSpSvcSetSvcTypeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeName.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeName.setDescription('The name of the Service Type associated with this table entry.')
jnxSpSvcSetSvcTypeSvcSets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeSvcSets.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeSvcSets.setDescription('The number of Service Sets configured on this Service PIC that use this service type.')
jnxSpSvcSetSvcTypeMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeMemoryUsage.setDescription('The amount of memory used by this Service Type, expressed in bytes.')
jnxSpSvcSetSvcTypePctMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 6), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypePctMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypePctMemoryUsage.setDescription('The amount of memory used by this Service Type, expressed as a percentage of the total.')
jnxSpSvcSetSvcTypeCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 7), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeCpuUtil.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeCpuUtil.setDescription('The amount of CPU used by this Service Type, expressed as a percentage of the total.')
jnxSpSvcSetSvcTypeMemoryUsage64 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 2, 1, 8), CounterBasedGauge64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeMemoryUsage64.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetSvcTypeMemoryUsage64.setDescription('The amount of memory used by this Service Type, expressed in bytes, represented by 64 bit integer.')
jnxSpSvcSetIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3), )
if mibBuilder.loadTexts: jnxSpSvcSetIfTable.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfTable.setDescription('Service Set data about each Service PIC on the router.')
jnxSpSvcSetIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxSpSvcSetIfEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfEntry.setDescription('Each entry provides Service Set information about a single Service PIC. Each Service PIC is identified by its corresponding ifIndex.')
jnxSpSvcSetIfTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfTableName.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfTableName.setDescription('The ifName of the interface identifying the Service PIC. If more than one interface is associated with the Service PIC, the name associated with the lowest layer interface is used for this object.')
jnxSpSvcSetIfSvcSets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfSvcSets.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfSvcSets.setDescription('The number of Service Sets configured on this Service PIC.')
jnxSpSvcSetIfMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 3), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryUsage.setDescription('The amount of memory used by this Service PIC, expressed in bytes.')
jnxSpSvcSetIfPctMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 4), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPctMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfPctMemoryUsage.setDescription('The amount of memory used by this Service PIC, expressed as a percentage of the total.')
jnxSpSvcSetIfPolMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 5), Gauge32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPolMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfPolMemoryUsage.setDescription('The amount of policy memory used by this Service PIC, expressed in bytes.')
jnxSpSvcSetIfPctPolMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 6), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPctPolMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfPctPolMemoryUsage.setDescription('The amount of policy memory used by this Service PIC, expressed as a percentage of the total.')
jnxSpSvcSetIfMemoryZone = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2), ("orange", 3), ("red", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryZone.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryZone.setDescription('The memory-usage zone currently occupied by this Service PIC. The definitions of each zone are: Green - All new flows are allowed. Yellow - Unused memory is reclaimed. All new flows are allowed. Orange - New flows are only allowed for service sets that are using less than their equal share of memory. Red - No new flows are allowed.')
jnxSpSvcSetIfCpuUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 8), Gauge32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfCpuUtil.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfCpuUtil.setDescription('The amount of CPU used by this Service PIC, expressed as a percentage of the total.')
jnxSpSvcSetIfMemoryUsage64 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 9), CounterBasedGauge64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryUsage64.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfMemoryUsage64.setDescription('The amount of memory used by this Service PIC, expressed in bytes, represented by 64 bit integer.')
jnxSpSvcSetIfPolMemoryUsage64 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 32, 1, 3, 1, 10), CounterBasedGauge64()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSpSvcSetIfPolMemoryUsage64.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetIfPolMemoryUsage64.setDescription('The amount of policy memory used by this Service PIC, expressed in bytes, represented by 64 bit integer.')
jnxSpNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0))
if mibBuilder.loadTexts: jnxSpNotificationPrefix.setStatus('current')
if mibBuilder.loadTexts: jnxSpNotificationPrefix.setDescription('All collector notifications are registered under this branch.')
jnxSpSvcSetZoneEntered = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 1)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetZoneEntered.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetZoneEntered.setDescription('This indicates a Service PIC has entered a more severe memory-usage zone from a less severe memory usage zone. The zone entered is identified by jnxSpSvcSetIfMemoryZone.')
jnxSpSvcSetZoneExited = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 2)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfMemoryZone"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetZoneExited.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetZoneExited.setDescription('This indicates a Service Pic has exited a more severe memory-usage zone to a less severe memory usage zone. The zone exited is identified by jnxSpSvcSetIfMemoryZone.')
jnxSpSvcSetCpuExceeded = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 3)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetCpuExceeded.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetCpuExceeded.setDescription('This indicates a Service Pic has exceeded its internal threshold for CPU utilization (85%).')
jnxSpSvcSetCpuOk = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 0, 4)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetIfCpuUtil"), ("JUNIPER-SP-MIB", "jnxSpSvcSetIfTableName"))
if mibBuilder.loadTexts: jnxSpSvcSetCpuOk.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetCpuOk.setDescription('This indicates a Service Pic has crossed below its internal threshold for CPU utilization (85%).')
jnxSpSvcSetFlowLimitUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitUtil.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitUtil.setDescription('The Total no of flows present in this Service Set, expressed as a percentage of the total maximum flows.')
jnxSpSvcSetNameUtil = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 32, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 96))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxSpSvcSetNameUtil.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetNameUtil.setDescription('The Service Set name.')
jnxSpSvcSetFlowLimitUtilized = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 32, 0, 1)).setObjects(("JUNIPER-SP-MIB", "jnxSpSvcSetFlowLimitUtil"), ("JUNIPER-SP-MIB", "jnxSpSvcSetNameUtil"))
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitUtilized.setStatus('current')
if mibBuilder.loadTexts: jnxSpSvcSetFlowLimitUtilized.setDescription('This indicates a Service Set has reached its upper limit of flows threshold of a maximun flows allowed for a service set.')
mibBuilder.exportSymbols("JUNIPER-SP-MIB", jnxSpSvcSetSvcTypeCpuUtil=jnxSpSvcSetSvcTypeCpuUtil, jnxSpSvcSetCpuLimitPktDrops=jnxSpSvcSetCpuLimitPktDrops, jnxSpSvcSetCpuUtil=jnxSpSvcSetCpuUtil, jnxSpSvcSetSvcTypeSvcSets=jnxSpSvcSetSvcTypeSvcSets, jnxSpSvcSetZoneEntered=jnxSpSvcSetZoneEntered, jnxSpSvcSetSvcTypePctMemoryUsage=jnxSpSvcSetSvcTypePctMemoryUsage, jnxSpSvcSet=jnxSpSvcSet, PYSNMP_MODULE_ID=jnxSpMIB, jnxSpSvcSetSvcTypeMemoryUsage=jnxSpSvcSetSvcTypeMemoryUsage, jnxSpSvcSetEntry=jnxSpSvcSetEntry, jnxSpNotificationPrefix=jnxSpNotificationPrefix, jnxSpSvcSetIfIndex=jnxSpSvcSetIfIndex, jnxSpSvcSetSvcTypeIndex=jnxSpSvcSetSvcTypeIndex, jnxSpSvcSetName=jnxSpSvcSetName, jnxSpNotifications=jnxSpNotifications, jnxSpSvcSetIfSvcSets=jnxSpSvcSetIfSvcSets, jnxSpSvcSetZoneExited=jnxSpSvcSetZoneExited, jnxSpSvcSetSvcTypeIfName=jnxSpSvcSetSvcTypeIfName, jnxSpSvcSetSvcType=jnxSpSvcSetSvcType, jnxSpSvcSetSvcTypeTable=jnxSpSvcSetSvcTypeTable, jnxSpSvcSetIfEntry=jnxSpSvcSetIfEntry, jnxSpSvcSetSvcTypeMemoryUsage64=jnxSpSvcSetSvcTypeMemoryUsage64, jnxSpSvcSetIfCpuUtil=jnxSpSvcSetIfCpuUtil, jnxSpSvcSetFlowLimitUtil=jnxSpSvcSetFlowLimitUtil, jnxSpSvcSetSvcStyle=jnxSpSvcSetSvcStyle, jnxSpSvcSetCpuExceeded=jnxSpSvcSetCpuExceeded, jnxSpMIB=jnxSpMIB, jnxSpSvcSetTable=jnxSpSvcSetTable, jnxSpSvcSetSvcTypeEntry=jnxSpSvcSetSvcTypeEntry, jnxSpSvcSetIfTableName=jnxSpSvcSetIfTableName, jnxSpSvcSetIfName=jnxSpSvcSetIfName, jnxSpSvcSetSvcTypeName=jnxSpSvcSetSvcTypeName, jnxSpSvcSetIfPctMemoryUsage=jnxSpSvcSetIfPctMemoryUsage, jnxSpSvcSetMemoryUsage=jnxSpSvcSetMemoryUsage, jnxSpSvcSetIfPolMemoryUsage=jnxSpSvcSetIfPolMemoryUsage, jnxFlowLimitTrapVars=jnxFlowLimitTrapVars, jnxSpSvcSetIfMemoryZone=jnxSpSvcSetIfMemoryZone, jnxSpSvcSetIfTable=jnxSpSvcSetIfTable, jnxSpSvcSetIfPctPolMemoryUsage=jnxSpSvcSetIfPctPolMemoryUsage, jnxSpSvcSetFlowLimitUtilized=jnxSpSvcSetFlowLimitUtilized, jnxSpSvcSetNameUtil=jnxSpSvcSetNameUtil, jnxSpSvcSetIfMemoryUsage=jnxSpSvcSetIfMemoryUsage, jnxSpSvcSetMemLimitPktDrops=jnxSpSvcSetMemLimitPktDrops, jnxSpSvcSetIfMemoryUsage64=jnxSpSvcSetIfMemoryUsage64, jnxSpSvcSetCpuOk=jnxSpSvcSetCpuOk, jnxSpSvcSetIfPolMemoryUsage64=jnxSpSvcSetIfPolMemoryUsage64, jnxSpSvcSetFlowLimitPktDrops=jnxSpSvcSetFlowLimitPktDrops, jnxSpSvcSetTypeIndex=jnxSpSvcSetTypeIndex)
