#
# PySNMP MIB module CISCO-VPC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VPC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, NotificationType, Gauge32, ObjectIdentity, Counter32, TimeTicks, ModuleIdentity, IpAddress, Counter64, MibIdentifier, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Gauge32", "ObjectIdentity", "Counter32", "TimeTicks", "ModuleIdentity", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVpcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 619))
ciscoVpcCapability.setRevisions(('2013-07-10 00:00',))
if mibBuilder.loadTexts: ciscoVpcCapability.setLastUpdated('201307100000Z')
if mibBuilder.loadTexts: ciscoVpcCapability.setOrganization('Cisco Systems, Inc.')
ciscoVpcCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 619, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpcCapNxOSV06R0202PN7K = ciscoVpcCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVpcCapNxOSV06R0202PN7K = ciscoVpcCapNxOSV06R0202PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VPC-CAPABILITY", ciscoVpcCapability=ciscoVpcCapability, ciscoVpcCapNxOSV06R0202PN7K=ciscoVpcCapNxOSV06R0202PN7K, PYSNMP_MODULE_ID=ciscoVpcCapability)
