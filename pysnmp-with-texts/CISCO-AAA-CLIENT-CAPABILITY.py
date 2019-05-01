#
# PySNMP MIB module CISCO-AAA-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:49:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, IpAddress, Bits, NotificationType, Unsigned32, Integer32, Counter64, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "IpAddress", "Bits", "NotificationType", "Unsigned32", "Integer32", "Counter64", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "MibIdentifier")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoAaaClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 322))
ciscoAaaClientCapability.setRevisions(('2004-02-03 00:00', '2003-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAaaClientCapability.setRevisionsDescriptions(('Added VARIATION for cacEnable and cacPrimaryMethod.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAaaClientCapability.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setDescription('The capabilities description of CISCO-AAA-CLIENT-MIB.')
ciscoAaaClientCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoAaaClientCapCatOSV08R0101.setDescription('CISCO-AAA-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-CAPABILITY", ciscoAaaClientCapability=ciscoAaaClientCapability, PYSNMP_MODULE_ID=ciscoAaaClientCapability, ciscoAaaClientCapCatOSV08R0101=ciscoAaaClientCapCatOSV08R0101)
