#
# PySNMP MIB module CISCO-VMPS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VMPS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, ObjectIdentity, iso, NotificationType, Bits, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Counter64, TimeTicks, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "iso", "NotificationType", "Bits", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVmpsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 365))
ciscoVmpsCapability.setRevisions(('2004-04-07 00:00', '2004-03-12 00:00', '2003-10-31 00:00',))
if mibBuilder.loadTexts: ciscoVmpsCapability.setLastUpdated('200404070000Z')
if mibBuilder.loadTexts: ciscoVmpsCapability.setOrganization('Cisco Systems, Inc.')
ciscoVmpsCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setStatus('current')
ciscoVmpsCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setStatus('current')
ciscoVmpsCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setStatus('current')
mibBuilder.exportSymbols("CISCO-VMPS-CAPABILITY", PYSNMP_MODULE_ID=ciscoVmpsCapability, ciscoVmpsCapCatOSV08R0301=ciscoVmpsCapCatOSV08R0301, ciscoVmpsCapCatOSV08R0101=ciscoVmpsCapCatOSV08R0101, ciscoVmpsCapability=ciscoVmpsCapability, ciscoVmpsCapCatOSV08R0401=ciscoVmpsCapCatOSV08R0401)
