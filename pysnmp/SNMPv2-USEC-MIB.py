#
# PySNMP MIB module SNMPv2-USEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMPv2-USEC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Unsigned32, Counter64, snmpModules, MibIdentifier, Bits, Gauge32, Counter32, TimeTicks, IpAddress, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Counter64", "snmpModules", "MibIdentifier", "Bits", "Gauge32", "Counter32", "TimeTicks", "IpAddress", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usecMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 6))
if mibBuilder.loadTexts: usecMIB.setLastUpdated('9601120000Z')
if mibBuilder.loadTexts: usecMIB.setOrganization('IETF SNMPv2 Working Group')
usecMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1))
class AgentID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

usecAgent = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1, 1))
agentID = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 1), AgentID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentID.setStatus('current')
agentBoots = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentBoots.setStatus('current')
agentTime = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: agentTime.setStatus('current')
agentSize = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(484, 65507))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSize.setStatus('current')
usecStats = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 1, 2))
usecStatsUnsupportedQoS = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnsupportedQoS.setStatus('current')
usecStatsNotInWindows = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsNotInWindows.setStatus('current')
usecStatsUnknownUserNames = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnknownUserNames.setStatus('current')
usecStatsWrongDigestValues = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsWrongDigestValues.setStatus('current')
usecStatsUnknownContexts = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnknownContexts.setStatus('current')
usecStatsBadParameters = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsBadParameters.setStatus('current')
usecStatsUnauthorizedOperations = MibScalar((1, 3, 6, 1, 6, 3, 6, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usecStatsUnauthorizedOperations.setStatus('current')
usecMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2))
usecMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2, 1))
usecMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 6, 2, 2))
usecMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 6, 2, 1, 1)).setObjects(("SNMPv2-USEC-MIB", "usecBasicGroup"), ("SNMPv2-USEC-MIB", "usecStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecMIBCompliance = usecMIBCompliance.setStatus('current')
usecBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 6, 2, 2, 1)).setObjects(("SNMPv2-USEC-MIB", "agentID"), ("SNMPv2-USEC-MIB", "agentBoots"), ("SNMPv2-USEC-MIB", "agentTime"), ("SNMPv2-USEC-MIB", "agentSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecBasicGroup = usecBasicGroup.setStatus('current')
usecStatsGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 6, 2, 2, 2)).setObjects(("SNMPv2-USEC-MIB", "usecStatsUnsupportedQoS"), ("SNMPv2-USEC-MIB", "usecStatsNotInWindows"), ("SNMPv2-USEC-MIB", "usecStatsUnknownUserNames"), ("SNMPv2-USEC-MIB", "usecStatsWrongDigestValues"), ("SNMPv2-USEC-MIB", "usecStatsUnknownContexts"), ("SNMPv2-USEC-MIB", "usecStatsBadParameters"), ("SNMPv2-USEC-MIB", "usecStatsUnauthorizedOperations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usecStatsGroup = usecStatsGroup.setStatus('current')
mibBuilder.exportSymbols("SNMPv2-USEC-MIB", PYSNMP_MODULE_ID=usecMIB, usecStatsUnauthorizedOperations=usecStatsUnauthorizedOperations, usecStatsGroup=usecStatsGroup, usecMIB=usecMIB, usecMIBConformance=usecMIBConformance, usecMIBGroups=usecMIBGroups, usecStatsNotInWindows=usecStatsNotInWindows, usecStatsUnknownContexts=usecStatsUnknownContexts, agentBoots=agentBoots, usecStatsUnknownUserNames=usecStatsUnknownUserNames, usecStatsBadParameters=usecStatsBadParameters, agentTime=agentTime, usecMIBCompliance=usecMIBCompliance, usecStats=usecStats, usecMIBObjects=usecMIBObjects, usecStatsWrongDigestValues=usecStatsWrongDigestValues, agentID=agentID, usecStatsUnsupportedQoS=usecStatsUnsupportedQoS, AgentID=AgentID, usecMIBCompliances=usecMIBCompliances, usecAgent=usecAgent, agentSize=agentSize, usecBasicGroup=usecBasicGroup)
