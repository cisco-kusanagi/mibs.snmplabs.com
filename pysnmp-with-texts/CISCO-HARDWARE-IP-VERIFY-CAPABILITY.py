#
# PySNMP MIB module CISCO-HARDWARE-IP-VERIFY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HARDWARE-IP-VERIFY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, iso, IpAddress, MibIdentifier, Integer32, Bits, Counter64, Gauge32, TimeTicks, ModuleIdentity, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "iso", "IpAddress", "MibIdentifier", "Integer32", "Bits", "Counter64", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoHardwareIpVerifyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 623))
ciscoHardwareIpVerifyCapability.setRevisions(('2013-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setLastUpdated('201307260000Z')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHardwareIpVerifyCapability.setDescription('Agent capabilities for CISCO-HARDWARE-IP-VERIFY-MIB.')
chivCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 623, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus \n                        7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chivCapNxOSV06R0104PN7k = chivCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: chivCapNxOSV06R0104PN7k.setDescription('CISCO-HARDWARE-IP-VERIFY-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-HARDWARE-IP-VERIFY-CAPABILITY", PYSNMP_MODULE_ID=ciscoHardwareIpVerifyCapability, chivCapNxOSV06R0104PN7k=chivCapNxOSV06R0104PN7k, ciscoHardwareIpVerifyCapability=ciscoHardwareIpVerifyCapability)
