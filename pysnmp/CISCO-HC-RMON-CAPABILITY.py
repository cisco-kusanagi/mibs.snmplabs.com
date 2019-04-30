#
# PySNMP MIB module CISCO-HC-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HC-RMON-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, IpAddress, MibIdentifier, ObjectIdentity, iso, TimeTicks, NotificationType, Gauge32, Bits, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "NotificationType", "Gauge32", "Bits", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHcRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 358))
ciscoHcRmonCapability.setRevisions(('2003-09-30 00:00',))
if mibBuilder.loadTexts: ciscoHcRmonCapability.setLastUpdated('200309300000Z')
if mibBuilder.loadTexts: ciscoHcRmonCapability.setOrganization('Cisco Systems, Inc.')
ciscoHcRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcRmonCapCatOSV08R0101 = ciscoHcRmonCapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-HC-RMON-CAPABILITY", ciscoHcRmonCapability=ciscoHcRmonCapability, ciscoHcRmonCapCatOSV08R0101=ciscoHcRmonCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoHcRmonCapability)
