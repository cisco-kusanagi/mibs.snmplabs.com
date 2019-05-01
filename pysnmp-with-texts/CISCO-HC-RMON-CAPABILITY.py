#
# PySNMP MIB module CISCO-HC-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HC-RMON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ModuleIdentity, MibIdentifier, Counter32, Bits, Unsigned32, iso, ObjectIdentity, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32", "Bits", "Unsigned32", "iso", "ObjectIdentity", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHcRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 358))
ciscoHcRmonCapability.setRevisions(('2003-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHcRmonCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHcRmonCapability.setLastUpdated('200309300000Z')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-rmon@cisco.com')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setDescription('The capabilities description of HC-RMON-MIB.')
ciscoHcRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoHcRmonCapCatOSV08R0101.setDescription('HC-RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-HC-RMON-CAPABILITY", ciscoHcRmonCapability=ciscoHcRmonCapability, PYSNMP_MODULE_ID=ciscoHcRmonCapability, ciscoHcRmonCapCatOSV08R0101=ciscoHcRmonCapCatOSV08R0101)
