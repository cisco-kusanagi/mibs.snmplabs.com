#
# PySNMP MIB module RIVERSTONE-RS93X-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-RS93X-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
riverstoneAgentCapabilities, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneAgentCapabilities")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, TimeTicks, Counter64, Integer32, Counter32, Gauge32, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "TimeTicks", "Counter64", "Integer32", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rstoneRs93xAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 10, 93))
rstoneRs93xAgentCapabilityMIB.setRevisions(('2002-11-15 00:00',))
if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setLastUpdated('200211250000Z')
if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setOrganization('Riverstone Networks, Inc')
rsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 10, 93, 1))
rs93x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 93, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs93x = rs93x.setProductRelease('9.3.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs93x = rs93x.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-RS93X-AGENTCAP-MIB", rsCapability=rsCapability, rstoneRs93xAgentCapabilityMIB=rstoneRs93xAgentCapabilityMIB, PYSNMP_MODULE_ID=rstoneRs93xAgentCapabilityMIB, rs93x=rs93x)
