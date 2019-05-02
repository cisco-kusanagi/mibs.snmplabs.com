#
# PySNMP MIB module CISCO-IPSEC-PROV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSEC-PROV-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Unsigned32, ModuleIdentity, ObjectIdentity, IpAddress, NotificationType, Counter32, MibIdentifier, TimeTicks, Bits, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIPsecProvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 486))
ciscoIPsecProvCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPsecProvCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIPsecProvCapability.setDescription('Agent capabilities for CISCO-IPSEC-PROVISIONING-MIB')
cIPsecProvCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 486, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecProvCapSanOSV30R1MDS9000 = cIPsecProvCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecProvCapSanOSV30R1MDS9000 = cIPsecProvCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIPsecProvCapSanOSV30R1MDS9000.setDescription('Cisco IPsec Provisioning MIB capabilities')
mibBuilder.exportSymbols("CISCO-IPSEC-PROV-CAPABILITY", cIPsecProvCapSanOSV30R1MDS9000=cIPsecProvCapSanOSV30R1MDS9000, PYSNMP_MODULE_ID=ciscoIPsecProvCapability, ciscoIPsecProvCapability=ciscoIPsecProvCapability)
