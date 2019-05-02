#
# PySNMP MIB module CISCO-QOS-PIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-QOS-PIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, ObjectIdentity, Counter64, iso, Counter32, MibIdentifier, ModuleIdentity, Bits, IpAddress, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "ObjectIdentity", "Counter64", "iso", "Counter32", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoQosPibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 390))
ciscoQosPibCapability.setRevisions(('2003-08-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoQosPibCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoQosPibCapability.setLastUpdated('200308140000Z')
if mibBuilder.loadTexts: ciscoQosPibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoQosPibCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoQosPibCapability.setDescription('The capabilities description of CISCO-QOS-PIB-MIB.')
ciscoQosPibCapCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 390, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPibCapCatOSV08R0101Cat6K = ciscoQosPibCapCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPibCapCatOSV08R0101Cat6K = ciscoQosPibCapCatOSV08R0101Cat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoQosPibCapCatOSV08R0101Cat6K.setDescription('CISCO-QOS-PIB-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-QOS-PIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoQosPibCapability, ciscoQosPibCapCatOSV08R0101Cat6K=ciscoQosPibCapCatOSV08R0101Cat6K, ciscoQosPibCapability=ciscoQosPibCapability)
