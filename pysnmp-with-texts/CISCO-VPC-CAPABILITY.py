#
# PySNMP MIB module CISCO-VPC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VPC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:19:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, TimeTicks, Bits, Counter32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, IpAddress, ModuleIdentity, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Bits", "Counter32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "ModuleIdentity", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVpcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 619))
ciscoVpcCapability.setRevisions(('2013-07-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVpcCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVpcCapability.setLastUpdated('201307100000Z')
if mibBuilder.loadTexts: ciscoVpcCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVpcCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVpcCapability.setDescription('The capabilities description of CISCO-VPC-MIB.')
ciscoVpcCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 619, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpcCapNxOSV06R0202PN7K = ciscoVpcCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpcCapNxOSV06R0202PN7K = ciscoVpcCapNxOSV06R0202PN7K.setStatus('current')
if mibBuilder.loadTexts: ciscoVpcCapNxOSV06R0202PN7K.setDescription('CISCO-VPC-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VPC-CAPABILITY", PYSNMP_MODULE_ID=ciscoVpcCapability, ciscoVpcCapNxOSV06R0202PN7K=ciscoVpcCapNxOSV06R0202PN7K, ciscoVpcCapability=ciscoVpcCapability)
