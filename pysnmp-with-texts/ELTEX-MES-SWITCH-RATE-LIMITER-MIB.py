#
# PySNMP MIB module ELTEX-MES-SWITCH-RATE-LIMITER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-SWITCH-RATE-LIMITER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:01:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
eltMesSwitchRateLimiterMIB, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesSwitchRateLimiterMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, IpAddress, MibIdentifier, Gauge32, Counter32, TimeTicks, Integer32, Unsigned32, ObjectIdentity, Counter64, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "IpAddress", "MibIdentifier", "Gauge32", "Counter32", "TimeTicks", "Integer32", "Unsigned32", "ObjectIdentity", "Counter64", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesSwitchRateLimiterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1))
eltMesSwitchRateLimiterConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1))
eltMesSwitchRateLimiterStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2))
class EltCpuRateLimiterTrafficType(TextualConvention, Integer32):
    description = 'Traffic types for rate limiting on CPU.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("http", 1), ("telnet", 2), ("ssh", 3), ("snmp", 4), ("ip", 5), ("linkLocal", 6), ("arp", 7), ("arpInspec", 8), ("stpBpdu", 9), ("otherBpdu", 10), ("ipRouting", 11), ("ipOptions", 12), ("dhcpSnoop", 13), ("igmpSnoop", 14), ("mldSnoop", 15), ("sflow", 16), ("ace", 17), ("ipErrors", 18), ("other", 19), ("dhcpv6Snoop", 20), ("vrrp", 21))

class EltCpuRateStatisticsTrafficType(TextualConvention, Integer32):
    description = 'Traffic types for input rates on CPU.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))
    namedValues = NamedValues(("stack", 1), ("http", 2), ("telnet", 3), ("ssh", 4), ("snmp", 5), ("ip", 6), ("arp", 7), ("arpInspec", 8), ("stp", 9), ("ieee", 10), ("routeUnknown", 11), ("ipHopByHop", 12), ("mtuExceeded", 13), ("ipv4Multicast", 14), ("ipv6Multicast", 15), ("dhcpSnooping", 16), ("igmpSnooping", 17), ("mldSnooping", 18), ("ttlExceeded", 19), ("ipv4IllegalAddress", 20), ("ipv4HeaderError", 21), ("ipDaMismatch", 22), ("sflow", 23), ("logDenyAces", 24), ("dhcpv6Snooping", 25), ("vrrp", 26), ("logPermitAces", 27), ("ipv6HeaderError", 28))

eltCpuRateLimiterTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1), )
if mibBuilder.loadTexts: eltCpuRateLimiterTable.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateLimiterTable.setDescription('A list of CPU rate limiters.')
eltCpuRateLimiterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1), ).setIndexNames((0, "ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateLimiterIndex"))
if mibBuilder.loadTexts: eltCpuRateLimiterEntry.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateLimiterEntry.setDescription('An entry containing the custom CPU rate limiter information for specific traffic type.')
eltCpuRateLimiterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 1), EltCpuRateLimiterTrafficType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuRateLimiterIndex.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateLimiterIndex.setDescription('Traffic type')
eltCpuRateLimiterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltCpuRateLimiterValue.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateLimiterValue.setDescription('Value of rate-limiter')
eltCpuRateStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1), )
if mibBuilder.loadTexts: eltCpuRateStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateStatisticsTable.setDescription('A list of CPU input rates per traffic type.')
eltCpuRateStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1), ).setIndexNames((0, "ELTEX-MES-SWITCH-RATE-LIMITER-MIB", "eltCpuRateStatisticsIndex"))
if mibBuilder.loadTexts: eltCpuRateStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateStatisticsEntry.setDescription('An entry containing the CPU input rates for specific traffic type.')
eltCpuRateStatisticsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 1), EltCpuRateStatisticsTrafficType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuRateStatisticsIndex.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateStatisticsIndex.setDescription('Traffic type')
eltCpuRateStatisticsRate = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuRateStatisticsRate.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateStatisticsRate.setDescription('Input rate int packets per second.')
eltCpuRateStatisticsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuRateStatisticsCounter.setStatus('current')
if mibBuilder.loadTexts: eltCpuRateStatisticsCounter.setDescription('Total counter of packets.')
mibBuilder.exportSymbols("ELTEX-MES-SWITCH-RATE-LIMITER-MIB", eltMesSwitchRateLimiterStatistics=eltMesSwitchRateLimiterStatistics, eltCpuRateStatisticsTable=eltCpuRateStatisticsTable, eltCpuRateStatisticsIndex=eltCpuRateStatisticsIndex, eltMesSwitchRateLimiterObjects=eltMesSwitchRateLimiterObjects, EltCpuRateStatisticsTrafficType=EltCpuRateStatisticsTrafficType, eltCpuRateStatisticsEntry=eltCpuRateStatisticsEntry, eltCpuRateLimiterEntry=eltCpuRateLimiterEntry, eltCpuRateStatisticsRate=eltCpuRateStatisticsRate, eltCpuRateLimiterTable=eltCpuRateLimiterTable, eltCpuRateLimiterIndex=eltCpuRateLimiterIndex, eltMesSwitchRateLimiterConfig=eltMesSwitchRateLimiterConfig, EltCpuRateLimiterTrafficType=EltCpuRateLimiterTrafficType, eltCpuRateLimiterValue=eltCpuRateLimiterValue, eltCpuRateStatisticsCounter=eltCpuRateStatisticsCounter)
