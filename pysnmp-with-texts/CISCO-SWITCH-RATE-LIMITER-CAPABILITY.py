#
# PySNMP MIB module CISCO-SWITCH-RATE-LIMITER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SWITCH-RATE-LIMITER-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, iso, IpAddress, TimeTicks, MibIdentifier, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, Unsigned32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "iso", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSwitchRateLimiterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 606))
ciscoSwitchRateLimiterCapability.setRevisions(('2011-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setLastUpdated('201107270000Z')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setDescription('The capabilities description of CISCO-SWITCH-RATE-LIMITER-MIB.')
ciscoRateLimiterCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 606, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setStatus('current')
if mibBuilder.loadTexts: ciscoRateLimiterCapNxOSV05R0201PN7k.setDescription('CISCO-SWITCH-RATE-LIMITER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-RATE-LIMITER-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchRateLimiterCapability, ciscoSwitchRateLimiterCapability=ciscoSwitchRateLimiterCapability, ciscoRateLimiterCapNxOSV05R0201PN7k=ciscoRateLimiterCapNxOSV05R0201PN7k)
