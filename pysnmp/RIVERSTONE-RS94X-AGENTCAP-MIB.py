#
# PySNMP MIB module RIVERSTONE-RS94X-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-RS94X-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
riverstoneAgentCapabilities, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneAgentCapabilities")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter32, Bits, Unsigned32, NotificationType, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, iso, ObjectIdentity, TimeTicks, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "iso", "ObjectIdentity", "TimeTicks", "IpAddress", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rstoneRs94xAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 10, 94))
rstoneRs94xAgentCapabilityMIB.setRevisions(('2003-06-21 00:00',))
if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setLastUpdated('200306210000Z')
if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setOrganization('Riverstone Networks, Inc')
rsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 10, 94, 1))
rs94x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 94, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs94x = rs94x.setProductRelease('9.4.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs94x = rs94x.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-RS94X-AGENTCAP-MIB", rs94x=rs94x, rstoneRs94xAgentCapabilityMIB=rstoneRs94xAgentCapabilityMIB, PYSNMP_MODULE_ID=rstoneRs94xAgentCapabilityMIB, rsCapability=rsCapability)
