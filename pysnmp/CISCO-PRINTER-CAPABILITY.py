#
# PySNMP MIB module CISCO-PRINTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRINTER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, NotificationType, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ObjectIdentity, Gauge32, MibIdentifier, ModuleIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ObjectIdentity", "Gauge32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrinterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 548))
ciscoPrinterCapability.setRevisions(('2007-06-07 00:00',))
if mibBuilder.loadTexts: ciscoPrinterCapability.setLastUpdated('200706070000Z')
if mibBuilder.loadTexts: ciscoPrinterCapability.setOrganization('Cisco Systems, Inc.')
ciscoPrinterCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 548, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setProductRelease('Cisco IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPrinterCapabilityV12R04 = ciscoPrinterCapabilityV12R04.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRINTER-CAPABILITY", ciscoPrinterCapabilityV12R04=ciscoPrinterCapabilityV12R04, ciscoPrinterCapability=ciscoPrinterCapability, PYSNMP_MODULE_ID=ciscoPrinterCapability)
