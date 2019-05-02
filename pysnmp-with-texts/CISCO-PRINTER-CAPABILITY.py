#
# PySNMP MIB module CISCO-PRINTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRINTER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, ModuleIdentity, NotificationType, Bits, Counter32, iso, Unsigned32, Counter64, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "ModuleIdentity", "NotificationType", "Bits", "Counter32", "iso", "Unsigned32", "Counter64", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrinterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 548))
ciscoPrinterCapability.setRevisions(('2007-06-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPrinterCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPrinterCapability.setLastUpdated('200706070000Z')
if mibBuilder.loadTexts: ciscoPrinterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPrinterCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPrinterCapability.setDescription('Agent capabilities for Printer-MIB')
ciscoPrinterCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 548, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoPrinterCapabilityV12R04.setDescription('Printer MIB capabilities')
mibBuilder.exportSymbols("CISCO-PRINTER-CAPABILITY", ciscoPrinterCapabilityV12R04=ciscoPrinterCapabilityV12R04, ciscoPrinterCapability=ciscoPrinterCapability, PYSNMP_MODULE_ID=ciscoPrinterCapability)
