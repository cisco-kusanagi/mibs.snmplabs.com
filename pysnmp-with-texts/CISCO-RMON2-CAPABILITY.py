#
# PySNMP MIB module CISCO-RMON2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RMON2-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, iso, ModuleIdentity, TimeTicks, Integer32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, IpAddress, Counter32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "ModuleIdentity", "TimeTicks", "Integer32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRmon2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 361))
ciscoRmon2Capability.setRevisions(('2003-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRmon2Capability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRmon2Capability.setLastUpdated('200310010000Z')
if mibBuilder.loadTexts: ciscoRmon2Capability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRmon2Capability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-rmon@cisco.com')
if mibBuilder.loadTexts: ciscoRmon2Capability.setDescription('The capabilities description of RMON2-MIB.')
ciscoRmon2CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 361, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmon2CapCatOSV08R0101 = ciscoRmon2CapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoRmon2CapCatOSV08R0101.setDescription('RMON2-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RMON2-CAPABILITY", PYSNMP_MODULE_ID=ciscoRmon2Capability, ciscoRmon2CapCatOSV08R0101=ciscoRmon2CapCatOSV08R0101, ciscoRmon2Capability=ciscoRmon2Capability)
