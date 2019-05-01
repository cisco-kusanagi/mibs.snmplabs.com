#
# PySNMP MIB module CISCO-VMPS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VMPS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, ModuleIdentity, Counter32, Gauge32, Unsigned32, Bits, ObjectIdentity, IpAddress, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter32", "Gauge32", "Unsigned32", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVmpsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 365))
ciscoVmpsCapability.setRevisions(('2004-04-07 00:00', '2004-03-12 00:00', '2003-10-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVmpsCapability.setRevisionsDescriptions(('Added capability statement ciscoVmpsCapCatOSV08R0401.', 'Added capability statement ciscoVmpsCapCatOSV08R0301.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVmpsCapability.setLastUpdated('200404070000Z')
if mibBuilder.loadTexts: ciscoVmpsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVmpsCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-vlans@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVmpsCapability.setDescription('The capabilities description of CISCO-VMPS-MIB.')
ciscoVmpsCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0101 = ciscoVmpsCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoVmpsCapCatOSV08R0101.setDescription('CISCO-VMPS-MIB capabilities.')
ciscoVmpsCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0301 = ciscoVmpsCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoVmpsCapCatOSV08R0301.setDescription('CISCO-VMPS-MIB capabilities.')
ciscoVmpsCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 365, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVmpsCapCatOSV08R0401 = ciscoVmpsCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoVmpsCapCatOSV08R0401.setDescription('CISCO-VMPS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VMPS-CAPABILITY", ciscoVmpsCapability=ciscoVmpsCapability, ciscoVmpsCapCatOSV08R0401=ciscoVmpsCapCatOSV08R0401, ciscoVmpsCapCatOSV08R0301=ciscoVmpsCapCatOSV08R0301, PYSNMP_MODULE_ID=ciscoVmpsCapability, ciscoVmpsCapCatOSV08R0101=ciscoVmpsCapCatOSV08R0101)
