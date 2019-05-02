#
# PySNMP MIB module OA-ZBFW-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OA-ZBFW-STATUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
oacExpIMZbFw, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMZbFw", "oacMIBModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, Gauge32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, Counter32, ModuleIdentity, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "Counter32", "ModuleIdentity", "NotificationType", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacZbfwStatusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 2003))
if mibBuilder.loadTexts: oacZbfwStatusMIB.setLastUpdated('201012160001Z')
if mibBuilder.loadTexts: oacZbfwStatusMIB.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacZbfwStatusMIB.setContactInfo(' OneAccess Belgium')
if mibBuilder.loadTexts: oacZbfwStatusMIB.setDescription('The oacZbfwStatusMIB')
class TableIndex(Unsigned32):
    pass

oacZbfw = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131))
oacZbfwPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12))
oacZbfwRtrConnPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40))
oacZbfwRtrConnPerfSSCTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1), )
if mibBuilder.loadTexts: oacZbfwRtrConnPerfSSCTable.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRtrConnPerfSSCTable.setDescription('router connection statistics')
oacZbfwRtrConnPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1), ).setIndexNames((1, "OA-ZBFW-STATUS-MIB", "oacZbfwRtrConnPerfGlobalIx"))
if mibBuilder.loadTexts: oacZbfwRtrConnPerfEntry.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRtrConnPerfEntry.setDescription('An index into the table of oacZbfwRtrConnPer')
oacZbfwRtrConnPerfGlobalIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 10), SnmpAdminString())
if mibBuilder.loadTexts: oacZbfwRtrConnPerfGlobalIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRtrConnPerfGlobalIx.setDescription('The value of the tlsCntTreeGlobalIndex of the MANAGED OBJECT.')
oacZbfwRouterConnectionsCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwRouterConnectionsCreated.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRouterConnectionsCreated.setDescription('Number of (half-open) connections created by the zone-based firewall.')
oacZbfwRouterConnectionsClosed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwRouterConnectionsClosed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRouterConnectionsClosed.setDescription('Number of zone-based firewall connections or half-open connections closed by a protocol or explicitly by a user.')
oacZbfwRouterConnectionsTimedOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwRouterConnectionsTimedOut.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRouterConnectionsTimedOut.setDescription('Number of zone-based firewall connections or half-open connections that timed out.')
oacZbfwRouterConnectionsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwRouterConnectionsMax.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRouterConnectionsMax.setDescription('Max number of zone-based firewall connections or half-open connections allowed in this instance.')
oacZbfwRouterConnectionsMaxUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwRouterConnectionsMaxUsed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRouterConnectionsMaxUsed.setDescription('Highest number of zone-based firewall connections or half-open connections that were simultaneously in use.')
oacZbfwRouterConnectionsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwRouterConnectionsUsed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwRouterConnectionsUsed.setDescription('Number of zone-based firewall connections or half-open connections that are currenlty in use.')
oacZbfwPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41))
oacZbfwPacketsSSCTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1), )
if mibBuilder.loadTexts: oacZbfwPacketsSSCTable.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsSSCTable.setDescription('packet statistics')
oacZbfwPacketsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1), ).setIndexNames((1, "OA-ZBFW-STATUS-MIB", "oacZbfwPacketsGlobalIx"))
if mibBuilder.loadTexts: oacZbfwPacketsEntry.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsEntry.setDescription('Aggregated packet handling statistics of the zone-based firewall.')
oacZbfwPacketsGlobalIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 1), SnmpAdminString())
if mibBuilder.loadTexts: oacZbfwPacketsGlobalIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsGlobalIx.setDescription('The value of the tlsCntTreeGlobalIndex of the MANAGED OBJECT.')
oacZbfwPacketsProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsProcessed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsProcessed.setDescription('Number of packets processed by the zone-based firewall.')
oacZbfwPacketsPassed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsPassed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsPassed.setDescription('Number of packets passed by the zone-based firewall.')
oacZbfwPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsDropped.setDescription('Number of packets dropped by an explicit drop rule of the zone-based firewall.')
oacZbfwPacketsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejected.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejected.setDescription('Number of packets rejected by the zone-based firewall because of an invalid interface, no matching rule could be found, no connection could be created, a protocol violation or an alg violation.')
oacZbfwPacketsRejectStatsInvalidIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsInvalidIntf.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsInvalidIntf.setDescription('Number of packets rejected by the zone-based firewall because of a missing valid interface for the packet.')
oacZbfwPacketsRejectStatsNoPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsNoPolicy.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsNoPolicy.setDescription('Number of packets rejected by the zone-based firewall because of a missing matching policy database entry.')
oacZbfwPacketsRejectStatsNoConnSetup = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsNoConnSetup.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsNoConnSetup.setDescription('Number of packets rejected by the zone-based firewall because no connection could be created.')
oacZbfwPacketsRejectStatsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsProtocol.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsProtocol.setDescription('Number of packets rejected by the zone-based firewall because of a protocol violation.')
oacZbfwPacketsRejectStatsAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsAlg.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsAlg.setDescription('Number of packets rejected by the zone-based firewall because of an alg violation.')
oacZbfwPacketsRejectStatsConnExceeded = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsConnExceeded.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPacketsRejectStatsConnExceeded.setDescription('Number of packets rejected by the zone-based firewall because the maximum number of connections was reached.')
oacZbfwPolicyRules = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42))
oacZbfwPolicyRulesSSCTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1), )
if mibBuilder.loadTexts: oacZbfwPolicyRulesSSCTable.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesSSCTable.setDescription('open policyrules perf')
oacZbfwPolicyRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1), ).setIndexNames((0, "OA-ZBFW-STATUS-MIB", "oacZbfwPolicyRulesTableIx"), (1, "OA-ZBFW-STATUS-MIB", "oacZbfwPolicyRulesGlobalIx"))
if mibBuilder.loadTexts: oacZbfwPolicyRulesEntry.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesEntry.setDescription('')
oacZbfwPolicyRulesTableIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 1), TableIndex())
if mibBuilder.loadTexts: oacZbfwPolicyRulesTableIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesTableIx.setDescription('The table of oacZbfwPolicyRules objects')
oacZbfwPolicyRulesGlobalIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 2), SnmpAdminString())
if mibBuilder.loadTexts: oacZbfwPolicyRulesGlobalIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesGlobalIx.setDescription('The value of the tlsCntTreeGlobalIndex of the MANAGED OBJECT.')
oacZbfwPolicyRulesZonePair = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesZonePair.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesZonePair.setDescription('Name of the zone-pair of this policy rule instance.')
oacZbfwPolicyRulesPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesPolicy.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesPolicy.setDescription('Name of the policy of this policy rule instance.')
oacZbfwPolicyRulesPolicyRule = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesPolicyRule.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesPolicyRule.setDescription('Name of the policy rule instance.')
oacZbfwPolicyRulesCountersProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersProcessed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersProcessed.setDescription('Number of times this policy rule instance was checked for packet matching.')
oacZbfwPolicyRulesCountersApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersApplied.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersApplied.setDescription('Number of times this policy rule instance was part of a matching policy database rule instance.')
oacZbfwPolicyRulesCountersConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersConnections.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersConnections.setDescription('Number of connections created from a matching policy database entry containing this policy rule instance.')
oacZbfwPolicyRulesCountersPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersPackets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersPackets.setDescription('Number of packets processed in a flow that was created from a matching policy database entry containing this policy rule instance.')
oacZbfwPolicyRulesCountersOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersOctets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersOctets.setDescription('Number of octets processed in a flow that was created from a matching policy database entry containing this policy rule instance.')
oacZbfwPolicyRulesCountersReversePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersReversePackets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersReversePackets.setDescription('Number of packets processed in a reverse flow that was created from a matching policy database entry containing this policy rule instance.')
oacZbfwPolicyRulesCountersReverseOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersReverseOctets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwPolicyRulesCountersReverseOctets.setDescription('Number of octets processed in a reverse flow that was created from a matching policy database entry containing this policy rule instance.')
oacZbfwClearCounters = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 43), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacZbfwClearCounters.setStatus('current')
if mibBuilder.loadTexts: oacZbfwClearCounters.setDescription('Clear firewall statistics and policy database counters.')
oacZbfwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14))
oacZbfwZonePairs = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22))
oacZbfwZonePairsSSCTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1), )
if mibBuilder.loadTexts: oacZbfwZonePairsSSCTable.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsSSCTable.setDescription('runtime zone pair status table')
oacZbfwZonePairsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1), ).setIndexNames((0, "OA-ZBFW-STATUS-MIB", "oacZbfwZonePairsTableIx"), (1, "OA-ZBFW-STATUS-MIB", "oacZbfwZonePairsGlobalIx"))
if mibBuilder.loadTexts: oacZbfwZonePairsEntry.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsEntry.setDescription('Zone-pair entry in the runtime policy database.')
oacZbfwZonePairsTableIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 1), TableIndex())
if mibBuilder.loadTexts: oacZbfwZonePairsTableIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsTableIx.setDescription('The table of oacZbfwZonePairs objects')
oacZbfwZonePairsGlobalIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 2), SnmpAdminString())
if mibBuilder.loadTexts: oacZbfwZonePairsGlobalIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsGlobalIx.setDescription('The value of the tlsCntTreeGlobalIndex of the MANAGED OBJECT.')
oacZbfwZonePairsName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsName.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsName.setDescription('Name of the zone-pair.')
oacZbfwZonePairsSrcZone = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsSrcZone.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsSrcZone.setDescription('Name of the source zone of this zone-pair.')
oacZbfwZonePairsDstZone = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsDstZone.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsDstZone.setDescription('Name of the destination zone of this zone-pair.')
oacZbfwZonePairsPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsPolicy.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsPolicy.setDescription('Name of the policy used for this zone-pair.')
oacZbfwZonePairsCountersProcessed = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersProcessed.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersProcessed.setDescription('Number of times this zone-pair instance was checked for packet matching.')
oacZbfwZonePairsCountersApplied = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersApplied.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersApplied.setDescription('Number of times this zone-pair instance was part of a matching policy database rule.')
oacZbfwZonePairsCountersConnections = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersConnections.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersConnections.setDescription('Number of connections created from a matching policy database entry containing this zone-pair.')
oacZbfwZonePairsCountersPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersPackets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersPackets.setDescription('Number of packets processed in a flow that was created from a matching policy database entry containing this zone-pair instance.')
oacZbfwZonePairsCountersOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersOctets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersOctets.setDescription('Number of octets processed in a flow that was created from a matching policy database entry containing this zone-pair instance.')
oacZbfwZonePairsCountersReversePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersReversePackets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersReversePackets.setDescription('Number of packets processed in a reverse flow that was created from a matching policy database entry containing this zone-pair instance.')
oacZbfwZonePairsCountersReverseOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwZonePairsCountersReverseOctets.setStatus('current')
if mibBuilder.loadTexts: oacZbfwZonePairsCountersReverseOctets.setDescription('Number of octets processed in a reverse flow that was created from a matching policy database entry containing this zone-pair instance.')
oacZbfwFlows = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23))
oacZbfwFlowsSSCTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1), )
if mibBuilder.loadTexts: oacZbfwFlowsSSCTable.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsSSCTable.setDescription('open flow status')
oacZbfwFlowsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1), ).setIndexNames((0, "OA-ZBFW-STATUS-MIB", "oacZbfwFlowsTableIx"), (1, "OA-ZBFW-STATUS-MIB", "oacZbfwFlowsGlobalIx"))
if mibBuilder.loadTexts: oacZbfwFlowsEntry.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsEntry.setDescription('Open flow.')
oacZbfwFlowsTableIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 1), TableIndex())
if mibBuilder.loadTexts: oacZbfwFlowsTableIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsTableIx.setDescription(' The table of oacZbfwFlows objects')
oacZbfwFlowsGlobalIx = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 2), SnmpAdminString())
if mibBuilder.loadTexts: oacZbfwFlowsGlobalIx.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsGlobalIx.setDescription('The value of the tlsCntTreeGlobalIndex of the MANAGED OBJECT.')
oacZbfwFlowsConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsConnectionId.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsConnectionId.setDescription('Unique Id of the connection this flow belongs to.')
oacZbfwFlowsSrcIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsSrcIntf.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsSrcIntf.setDescription('Name of the source interface of a flow.')
oacZbfwFlowsSrcZone = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsSrcZone.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsSrcZone.setDescription('Name of the source zone of a flow.')
oacZbfwFlowsDstIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsDstIntf.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsDstIntf.setDescription('Name of the destination interface of a flow.')
oacZbfwFlowsDstZone = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsDstZone.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsDstZone.setDescription('Name of the destination zone of a flow.')
oacZbfwFlowsSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsSrcAddress.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsSrcAddress.setDescription('Source address of a flow.')
oacZbfwFlowsDstAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsDstAddress.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsDstAddress.setDescription('Destination address of a flow.')
oacZbfwFlowsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 51, 8, 50, 47, 1, 9, 2, 88, 4, 89, 17, 46, 6))).clone(namedValues=NamedValues(("any", 0), ("ah", 51), ("egp", 8), ("esp", 50), ("gre", 47), ("icmp", 1), ("igp", 9), ("igmp", 2), ("igrp", 88), ("ipInIp", 4), ("ospf", 89), ("udp", 17), ("rsvp", 46), ("tcp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsProtocol.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsProtocol.setDescription('Protocol of a flow. Possibilities: any (0) ah (51) egp (8) esp (50) gre (47) icmp (1) igp (9) igmp (2) igrp (88) ipInIp (4) ospf (89) udp (17) rsvp (46) tcp (6)')
oacZbfwFlowsSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsSrcPort.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsSrcPort.setDescription('Source port number of a flow.')
oacZbfwFlowsDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsDstPort.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsDstPort.setDescription('Destination port number of a flow.')
oacZbfwFlowsAge = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsAge.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsAge.setDescription('Age of a flow.')
oacZbfwFlowsTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsTimeOut.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsTimeOut.setDescription('Remaining time before a flow goes in timeout and will be removed.')
oacZbfwFlowsRulesZonePair = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsRulesZonePair.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsRulesZonePair.setDescription('Name of the zone-pair matching with a flow.')
oacZbfwFlowsRulesPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsRulesPolicy.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsRulesPolicy.setDescription('Name of the policy matching with a flow.')
oacZbfwFlowsRulesPolicyRule = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsRulesPolicyRule.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsRulesPolicyRule.setDescription('Name of the policy rule matching with a flow.')
oacZbfwFlowsRulesFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsRulesFilter.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsRulesFilter.setDescription('Name of the filter matching with a flow.')
oacZbfwFlowsRulesFilterRule = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsRulesFilterRule.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsRulesFilterRule.setDescription('Name of the filter rule matching with a flow.')
oacZbfwFlowsModeAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacZbfwFlowsModeAlg.setStatus('current')
if mibBuilder.loadTexts: oacZbfwFlowsModeAlg.setDescription('Boolean indicating if a flow is created by an Alg.')
mibBuilder.exportSymbols("OA-ZBFW-STATUS-MIB", oacZbfwFlowsTimeOut=oacZbfwFlowsTimeOut, oacZbfwZonePairsSSCTable=oacZbfwZonePairsSSCTable, oacZbfwZonePairsCountersConnections=oacZbfwZonePairsCountersConnections, oacZbfwPacketsPassed=oacZbfwPacketsPassed, oacZbfwPacketsProcessed=oacZbfwPacketsProcessed, oacZbfwPolicyRulesCountersProcessed=oacZbfwPolicyRulesCountersProcessed, oacZbfwFlows=oacZbfwFlows, oacZbfwFlowsAge=oacZbfwFlowsAge, oacZbfw=oacZbfw, oacZbfwFlowsRulesFilterRule=oacZbfwFlowsRulesFilterRule, oacZbfwFlowsSrcZone=oacZbfwFlowsSrcZone, oacZbfwPacketsRejectStatsConnExceeded=oacZbfwPacketsRejectStatsConnExceeded, oacZbfwFlowsSrcPort=oacZbfwFlowsSrcPort, oacZbfwPacketsSSCTable=oacZbfwPacketsSSCTable, oacZbfwZonePairsName=oacZbfwZonePairsName, oacZbfwFlowsRulesFilter=oacZbfwFlowsRulesFilter, oacZbfwStatus=oacZbfwStatus, oacZbfwPacketsGlobalIx=oacZbfwPacketsGlobalIx, oacZbfwRtrConnPerfEntry=oacZbfwRtrConnPerfEntry, oacZbfwPackets=oacZbfwPackets, oacZbfwRouterConnectionsCreated=oacZbfwRouterConnectionsCreated, oacZbfwPacketsRejectStatsNoPolicy=oacZbfwPacketsRejectStatsNoPolicy, oacZbfwRouterConnectionsClosed=oacZbfwRouterConnectionsClosed, oacZbfwFlowsSSCTable=oacZbfwFlowsSSCTable, oacZbfwPacketsRejectStatsNoConnSetup=oacZbfwPacketsRejectStatsNoConnSetup, oacZbfwPolicyRules=oacZbfwPolicyRules, oacZbfwZonePairsTableIx=oacZbfwZonePairsTableIx, oacZbfwZonePairsGlobalIx=oacZbfwZonePairsGlobalIx, oacZbfwPolicyRulesCountersReverseOctets=oacZbfwPolicyRulesCountersReverseOctets, oacZbfwRtrConnPerfSSCTable=oacZbfwRtrConnPerfSSCTable, oacZbfwPacketsRejectStatsAlg=oacZbfwPacketsRejectStatsAlg, oacZbfwZonePairsCountersReverseOctets=oacZbfwZonePairsCountersReverseOctets, oacZbfwClearCounters=oacZbfwClearCounters, oacZbfwZonePairsDstZone=oacZbfwZonePairsDstZone, oacZbfwFlowsConnectionId=oacZbfwFlowsConnectionId, oacZbfwPolicyRulesSSCTable=oacZbfwPolicyRulesSSCTable, oacZbfwPolicyRulesCountersConnections=oacZbfwPolicyRulesCountersConnections, oacZbfwFlowsProtocol=oacZbfwFlowsProtocol, oacZbfwPacketsRejected=oacZbfwPacketsRejected, oacZbfwFlowsDstZone=oacZbfwFlowsDstZone, oacZbfwRouterConnectionsMax=oacZbfwRouterConnectionsMax, oacZbfwFlowsTableIx=oacZbfwFlowsTableIx, oacZbfwFlowsSrcIntf=oacZbfwFlowsSrcIntf, oacZbfwPolicyRulesCountersPackets=oacZbfwPolicyRulesCountersPackets, oacZbfwFlowsRulesPolicy=oacZbfwFlowsRulesPolicy, oacZbfwRouterConnectionsMaxUsed=oacZbfwRouterConnectionsMaxUsed, oacZbfwZonePairsEntry=oacZbfwZonePairsEntry, oacZbfwRtrConnPerf=oacZbfwRtrConnPerf, oacZbfwZonePairsCountersReversePackets=oacZbfwZonePairsCountersReversePackets, oacZbfwRouterConnectionsTimedOut=oacZbfwRouterConnectionsTimedOut, oacZbfwZonePairs=oacZbfwZonePairs, oacZbfwPolicyRulesGlobalIx=oacZbfwPolicyRulesGlobalIx, oacZbfwPolicyRulesZonePair=oacZbfwPolicyRulesZonePair, oacZbfwStatusMIB=oacZbfwStatusMIB, oacZbfwPolicyRulesTableIx=oacZbfwPolicyRulesTableIx, oacZbfwFlowsRulesZonePair=oacZbfwFlowsRulesZonePair, oacZbfwFlowsDstIntf=oacZbfwFlowsDstIntf, oacZbfwPacketsEntry=oacZbfwPacketsEntry, oacZbfwPerf=oacZbfwPerf, oacZbfwFlowsGlobalIx=oacZbfwFlowsGlobalIx, oacZbfwPolicyRulesPolicyRule=oacZbfwPolicyRulesPolicyRule, TableIndex=TableIndex, oacZbfwFlowsDstAddress=oacZbfwFlowsDstAddress, oacZbfwPacketsRejectStatsInvalidIntf=oacZbfwPacketsRejectStatsInvalidIntf, oacZbfwZonePairsPolicy=oacZbfwZonePairsPolicy, oacZbfwFlowsEntry=oacZbfwFlowsEntry, oacZbfwPolicyRulesCountersReversePackets=oacZbfwPolicyRulesCountersReversePackets, oacZbfwPacketsDropped=oacZbfwPacketsDropped, oacZbfwRouterConnectionsUsed=oacZbfwRouterConnectionsUsed, oacZbfwZonePairsSrcZone=oacZbfwZonePairsSrcZone, oacZbfwPolicyRulesCountersApplied=oacZbfwPolicyRulesCountersApplied, oacZbfwFlowsModeAlg=oacZbfwFlowsModeAlg, oacZbfwZonePairsCountersProcessed=oacZbfwZonePairsCountersProcessed, oacZbfwFlowsRulesPolicyRule=oacZbfwFlowsRulesPolicyRule, oacZbfwZonePairsCountersOctets=oacZbfwZonePairsCountersOctets, oacZbfwZonePairsCountersApplied=oacZbfwZonePairsCountersApplied, oacZbfwPolicyRulesCountersOctets=oacZbfwPolicyRulesCountersOctets, oacZbfwPolicyRulesEntry=oacZbfwPolicyRulesEntry, oacZbfwFlowsDstPort=oacZbfwFlowsDstPort, oacZbfwPolicyRulesPolicy=oacZbfwPolicyRulesPolicy, oacZbfwZonePairsCountersPackets=oacZbfwZonePairsCountersPackets, oacZbfwRtrConnPerfGlobalIx=oacZbfwRtrConnPerfGlobalIx, oacZbfwFlowsSrcAddress=oacZbfwFlowsSrcAddress, PYSNMP_MODULE_ID=oacZbfwStatusMIB, oacZbfwPacketsRejectStatsProtocol=oacZbfwPacketsRejectStatsProtocol)
