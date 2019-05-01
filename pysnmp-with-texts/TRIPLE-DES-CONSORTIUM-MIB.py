#
# PySNMP MIB module TRIPLE-DES-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRIPLE-DES-CONSORTIUM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, IpAddress, ObjectIdentity, MibIdentifier, snmpModules, TimeTicks, enterprises, Counter32, NotificationType, iso, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "ObjectIdentity", "MibIdentifier", "snmpModules", "TimeTicks", "enterprises", "Counter32", "NotificationType", "iso", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity")
AutonomousType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "TextualConvention")
tripleDESConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
tripleDESConsortiumMIB.setRevisions(('2003-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tripleDESConsortiumMIB.setRevisionsDescriptions(('Initial version, published as an Internet Draft.',))
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setLastUpdated('200302030000Z')
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setOrganization('Triple DES Consortium')
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setContactInfo('?')
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setDescription("Extension to the SNMP User-based Security Model to support Triple-DES EDE in 'Outside' CBC (cipher-block chaining) Mode. ")
tripleDESConsortiumPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
if mibBuilder.loadTexts: usm3DESPrivProtocol.setDescription('The 3DES-EDE Symmetric Encryption Protocol.')
if mibBuilder.loadTexts: usm3DESPrivProtocol.setReference('- Data Encryption Standard, National Institute of Standards and Technology. Federal Information Processing Standard (FIPS) Publication 46-3, (1999, pending approval). Will supersede FIPS Publication 46-2. - Data Encryption Algorithm, American National Standards Institute. ANSI X3.92-1981, (December, 1980). - DES Modes of Operation, National Institute of Standards and Technology. Federal Information Processing Standard (FIPS) Publication 81, (December, 1980). - Data Encryption Algorithm - Modes of Operation, American National Standards Institute. ANSI X3.106-1983, (May 1983). ')
mibBuilder.exportSymbols("TRIPLE-DES-CONSORTIUM-MIB", tripleDESConsortiumPrivProtocols=tripleDESConsortiumPrivProtocols, PYSNMP_MODULE_ID=tripleDESConsortiumMIB, tripleDESConsortiumMIB=tripleDESConsortiumMIB, usm3DESPrivProtocol=usm3DESPrivProtocol)
