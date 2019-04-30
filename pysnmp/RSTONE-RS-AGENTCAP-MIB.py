#
# PySNMP MIB module RSTONE-RS-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RSTONE-RS-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
riverstoneAgentCapabilities, = mibBuilder.importSymbols("RSTONE-SMI-MIB", "riverstoneAgentCapabilities")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, MibIdentifier, Counter32, Counter64, iso, IpAddress, ModuleIdentity, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "MibIdentifier", "Counter32", "Counter64", "iso", "IpAddress", "ModuleIdentity", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rstoneRsAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 10, 1))
rstoneRsAgentCapabilityMIB.setRevisions(('2001-06-21 00:00', '2001-03-11 00:00', '2001-03-07 00:00', '2000-12-13 00:00', '2000-09-18 00:00', '2000-09-12 00:00',))
if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setLastUpdated('200106210000Z')
if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setOrganization('Riverstone Networks, Inc')
rsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1))
rs61x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs61x = rs61x.setProductRelease('6.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs61x = rs61x.setStatus('current')
rs62x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs62x = rs62x.setProductRelease('6.2.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs62x = rs62x.setStatus('current')
rs63x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs63x = rs63x.setProductRelease('6.3.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs63x = rs63x.setStatus('current')
rs70x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs70x = rs70x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs70x = rs70x.setStatus('current')
rs80x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs80x = rs80x.setProductRelease('8.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs80x = rs80x.setStatus('current')
mibBuilder.exportSymbols("RSTONE-RS-AGENTCAP-MIB", rsCapability=rsCapability, PYSNMP_MODULE_ID=rstoneRsAgentCapabilityMIB, rs61x=rs61x, rs63x=rs63x, rs62x=rs62x, rs80x=rs80x, rstoneRsAgentCapabilityMIB=rstoneRsAgentCapabilityMIB, rs70x=rs70x)
