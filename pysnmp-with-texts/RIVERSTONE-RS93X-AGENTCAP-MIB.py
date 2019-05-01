#
# PySNMP MIB module RIVERSTONE-RS93X-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-RS93X-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
riverstoneAgentCapabilities, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneAgentCapabilities")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, Unsigned32, IpAddress, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, ModuleIdentity, NotificationType, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Unsigned32", "IpAddress", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rstoneRs93xAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 10, 93))
rstoneRs93xAgentCapabilityMIB.setRevisions(('2002-11-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setRevisionsDescriptions(('Created agent capabilities mib for version 9.3.x of Riverstone RS RapidOS software product. For agent capabilities of older versions of RapidOS, refer to rstone-rs-agent-cap-mib.txt and ssr-agent-capabilities mib',))
if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setLastUpdated('200211250000Z')
if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rstoneRs93xAgentCapabilityMIB.setDescription('This module defines agent capabilities for Riverstone RS RapidOS Software Product version 9.3.x.')
rsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 10, 93, 1))
rs93x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 93, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs93x = rs93x.setProductRelease('9.3.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs93x = rs93x.setStatus('current')
if mibBuilder.loadTexts: rs93x.setDescription('Firmware Release 9.3.x for Riverstone RS RapidOS product line. This firmware version supports the following new features - Layer 2 VPLS based on Lasserre-Compella draft, RFC 2549 MPLS-BGP VPN support, ATM VC support for Martini VLL, and HRT enhancements. New hardware includes ES 10170 with Gen5 GE and Gen 4 FE blades, CM5 for RS 8000, OC3 and OC48 PoS/MPLS blades for RS 38000, PoS/MPLS blade for RS 3000, and FE Gen5 blades for RS 38000, RS 8000 and RS 3000. Changes in Existing MIB Modules include: DISMAN-PING-MIB New MIB modules include: RIVERSTONE-MPLS-MIB RIVERSTONE-QUEUE-MIB RIVERSTONE-VLAN-EXTENSIONS-MIB (introduced in release 9.1.0.1) ')
rs93x.setReference('http://www.riverstonenet.com/products')
mibBuilder.exportSymbols("RIVERSTONE-RS93X-AGENTCAP-MIB", PYSNMP_MODULE_ID=rstoneRs93xAgentCapabilityMIB, rsCapability=rsCapability, rs93x=rs93x, rstoneRs93xAgentCapabilityMIB=rstoneRs93xAgentCapabilityMIB)
