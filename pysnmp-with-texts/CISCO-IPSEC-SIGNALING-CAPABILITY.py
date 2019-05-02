#
# PySNMP MIB module CISCO-IPSEC-SIGNALING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSEC-SIGNALING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, Unsigned32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Bits, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "Unsigned32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Bits", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIPsecSigCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 488))
ciscoIPsecSigCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPsecSigCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIPsecSigCapability.setDescription('Agent capabilities for CISCO-IPSEC-SIGNALING-MIB')
cIPsecSigCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 488, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIPsecSigCapSanOSV30R1MDS9000 = cIPsecSigCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cIPsecSigCapSanOSV30R1MDS9000.setDescription('Cisco Generic IPsec/FC-SP Signaling MIB capabilities')
mibBuilder.exportSymbols("CISCO-IPSEC-SIGNALING-CAPABILITY", ciscoIPsecSigCapability=ciscoIPsecSigCapability, cIPsecSigCapSanOSV30R1MDS9000=cIPsecSigCapSanOSV30R1MDS9000, PYSNMP_MODULE_ID=ciscoIPsecSigCapability)
