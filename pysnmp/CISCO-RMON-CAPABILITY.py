#
# PySNMP MIB module CISCO-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RMON-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:54:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
IpAddress, Counter64, NotificationType, ModuleIdentity, ObjectIdentity, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Bits, Gauge32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Bits", "Gauge32", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 357))
ciscoRmonCapability.setRevisions(('2008-08-04 00:00', '2006-03-09 00:00', '2004-04-02 00:00',))
if mibBuilder.loadTexts: ciscoRmonCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoRmonCapability.setOrganization('Cisco Systems, Inc.')
ciscoRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setStatus('current')
ciscoRmonCapNXOSV04R0101PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setStatus('current')
mibBuilder.exportSymbols("CISCO-RMON-CAPABILITY", ciscoRmonCapNXOSV04R0101PMDS9000=ciscoRmonCapNXOSV04R0101PMDS9000, ciscoRmonCapCatOSV08R0101=ciscoRmonCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoRmonCapability, ciscoRmonCapability=ciscoRmonCapability)
