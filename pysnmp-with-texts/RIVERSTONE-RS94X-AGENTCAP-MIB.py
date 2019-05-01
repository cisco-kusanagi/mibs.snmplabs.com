#
# PySNMP MIB module RIVERSTONE-RS94X-AGENTCAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-RS94X-AGENTCAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:57:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
riverstoneAgentCapabilities, = mibBuilder.importSymbols("RIVERSTONE-SMI-MIB", "riverstoneAgentCapabilities")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, MibIdentifier, Unsigned32, ObjectIdentity, TimeTicks, Integer32, iso, NotificationType, ModuleIdentity, Counter32, Counter64, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Unsigned32", "ObjectIdentity", "TimeTicks", "Integer32", "iso", "NotificationType", "ModuleIdentity", "Counter32", "Counter64", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rstoneRs94xAgentCapabilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 10, 94))
rstoneRs94xAgentCapabilityMIB.setRevisions(('2003-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setRevisionsDescriptions((' Updated Agent capabilities for MIB modules in 9.4 release.',))
if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setLastUpdated('200306210000Z')
if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setOrganization('Riverstone Networks, Inc')
if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setContactInfo('Riverstone Networks, Inc 5200 Great America Parkway Santa Clara CA USA 95054 PHONE:+1 408.878.6500 EMAIL: nms-eng@riverstonenet.com WEB: http://www.riverstonenet.com')
if mibBuilder.loadTexts: rstoneRs94xAgentCapabilityMIB.setDescription('This module defines agent capabilities for Riverstone RS RapidOS Software Product version 9.4.x.')
rsCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 10, 94, 1))
rs94x = AgentCapabilities((1, 3, 6, 1, 4, 1, 5567, 10, 94, 1, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs94x = rs94x.setProductRelease('9.4.x')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs94x = rs94x.setStatus('current')
if mibBuilder.loadTexts: rs94x.setDescription('Firmware Release 9.4.x for Riverstone RS RapidOS product line. This firmware version supports the following new features - Advanced traffic shaping and rate-limiting, VPLS scalability enhancements. New hardware includes ASM - Advanced Services Module, RS 3100/3200/1100 with 5th gen ASICs. RS 3200 has two fixed 16 port 10/100 Ethernet FX cards. Changes in Existing MIB Modules include: RIVERSTONE-RL-MIB RIVERSTONE-PRODUCTS-MIB RIVERSTONE-INVENTORY-MIB RIVERSTONE-CONFIG-MIB RIVERSTONE-NOTIFICATIONS-MIB New MIB modules include: RIVERSTONE-PING-EXTENSIONS-MIB RIVERSTONE-TRACEROUTE-EXTENSIONS-MIB RIVERSTONE-IF-MIB RIVERSTONE-CAPACITY-MIB DHCP-SERVER-MIB ')
rs94x.setReference('http://www.riverstonenet.com/products')
mibBuilder.exportSymbols("RIVERSTONE-RS94X-AGENTCAP-MIB", rstoneRs94xAgentCapabilityMIB=rstoneRs94xAgentCapabilityMIB, rsCapability=rsCapability, rs94x=rs94x, PYSNMP_MODULE_ID=rstoneRs94xAgentCapabilityMIB)
