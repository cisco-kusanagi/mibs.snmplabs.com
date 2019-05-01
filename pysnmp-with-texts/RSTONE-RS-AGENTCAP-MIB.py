#
# PySNMP MIB module RSTONE-RS-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RSTONE-RS-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
riverstoneAgentCapabilities, = mibBuilder.importSymbols("RSTONE-SMI-MIB", "riverstoneAgentCapabilities")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, IpAddress, MibIdentifier, Unsigned32, Counter64, Integer32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "Counter64", "Integer32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rstoneRsAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 10, 1))
rstoneRsAgentCapabilityMIB.setRevisions(('2001-06-21 00:00', '2001-03-11 00:00', '2001-03-07 00:00', '2000-12-13 00:00', '2000-09-18 00:00', '2000-09-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setRevisionsDescriptions((' Updated Agent Capabilities for firmware release 8.0', ' Updated Agent Capabilities for firmware release 7.0', ' Fixed some errors in Agent Capabilities for firmware release 6.3', ' Updated Agent Capabilities for firmware release 6.2, 6.3', ' Updated Agent Capabilities for ATM-MIB for firmware release 6.1.x', 'Created agent capabilities mib for version 6.1.x of Riverstone RS RapidOS software product. For agent capabilities of older versions of RapidOS, refer ssr-agent-capabilities mib',))
if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setLastUpdated('200106210000Z')
if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rstoneRsAgentCapabilityMIB.setDescription('This module defines agent capabilities for Riverstone RS RapidOS Software Product.')
rsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1))
rs61x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs61x = rs61x.setProductRelease('6.1.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs61x = rs61x.setStatus('current')
if mibBuilder.loadTexts: rs61x.setDescription('Firmware Release 6.1.x for Riverstone RS RapidOS product line. The firmware supports Cable Modem Head End card in release 6.1 and ATM OC12 card in release 6.1.1')
rs61x.setReference('http://www.riverstonenet.com/products')
rs62x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs62x = rs62x.setProductRelease('6.2.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs62x = rs62x.setStatus('current')
if mibBuilder.loadTexts: rs62x.setDescription('Firmware Release 6.2.x for Riverstone RS RapidOS product line. The firmware supports channelized T1/E1 card in release 6.2')
rs62x.setReference('http://www.riverstonenet.com/products')
rs63x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs63x = rs63x.setProductRelease('6.3.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs63x = rs63x.setStatus('current')
if mibBuilder.loadTexts: rs63x.setDescription('Firmware Release 6.3.x for Riverstone RS RapidOS product line. The firmware supports channelized T3/E3 card in release 6.3')
rs63x.setReference('http://www.riverstonenet.com/products')
rs70x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs70x = rs70x.setProductRelease('7.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs70x = rs70x.setStatus('current')
if mibBuilder.loadTexts: rs70x.setDescription('Firmware Release 7.0.x for Riverstone RS RapidOS product line. The firmware supports RS 38000 in this release. New software features include rate limiting enhancements and stackable VLANs. New MIBs include RFC 2674 P/Q Bridge MIB SETs and IEEE LAG MIB')
rs70x.setReference('http://www.riverstonenet.com/products')
rs80x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 1, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs80x = rs80x.setProductRelease('8.0.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs80x = rs80x.setStatus('current')
if mibBuilder.loadTexts: rs80x.setDescription('Firmware Release 8.0.x for Riverstone RS RapidOS product line. The firmware supports RS 16000 in this release. It also supports MPLS hardware and software. Other software features include SLR, Unnumbered Interfaces, per VLAN statistics and Hot CM failover (phase 1). New MIBs include VLAN statistics in RFC 2674 Q Bridge MIB and rstone-atm-mib for learning MAC addresses on a per VC basis.')
rs80x.setReference('http://www.riverstonenet.com/products')
mibBuilder.exportSymbols("RSTONE-RS-AGENTCAP-MIB", rstoneRsAgentCapabilityMIB=rstoneRsAgentCapabilityMIB, rs80x=rs80x, rsCapability=rsCapability, rs61x=rs61x, PYSNMP_MODULE_ID=rstoneRsAgentCapabilityMIB, rs63x=rs63x, rs70x=rs70x, rs62x=rs62x)
