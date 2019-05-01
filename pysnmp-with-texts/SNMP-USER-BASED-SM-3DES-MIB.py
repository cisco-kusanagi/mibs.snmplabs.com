#
# PySNMP MIB module SNMP-USER-BASED-SM-3DES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-USER-BASED-SM-3DES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
snmpPrivProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpPrivProtocols")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, ObjectIdentity, snmpModules, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, IpAddress, Counter32, iso, NotificationType, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ObjectIdentity", "snmpModules", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "IpAddress", "Counter32", "iso", "NotificationType", "Unsigned32", "MibIdentifier")
AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString")
snmpUsmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 15))
snmpUsmMIB.setRevisions(('1999-10-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpUsmMIB.setRevisionsDescriptions(('Initial version, published as an Internet Draft.',))
if mibBuilder.loadTexts: snmpUsmMIB.setLastUpdated('9910060000Z')
if mibBuilder.loadTexts: snmpUsmMIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpUsmMIB.setContactInfo('WG-email: snmpv3@lists.tislabs.com Subscribe: majordomo@lists.tislabs.com In msg body: subscribe snmpv3 Chair: Russ Mundy NAI Labs postal: 3060 Washington Rd Glenwood MD 21738 USA email: mundy@tislabs.com phone: +1-443-259-2307 Co-editor: David Reeder NAI Labs postal: 3060 Washington Road (Route 97) Glenwood, MD 21738 USA email: dreeder@tislabs.com phone: +1-443-259-2348 Co-editor: Olafur Gudmundsson NAI Labs postal: 3060 Washington Road (Route 97) Glenwood, MD 21738 USA email: ogud@tislabs.com phone: +1-443-259-2389 ')
if mibBuilder.loadTexts: snmpUsmMIB.setDescription("Extension to the SNMP User-based Security Model to support Triple-DES EDE in 'Outside' CBC (cipher-block chaining) Mode. ")
usm3DESEDEPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 3))
if mibBuilder.loadTexts: usm3DESEDEPrivProtocol.setStatus('current')
if mibBuilder.loadTexts: usm3DESEDEPrivProtocol.setDescription('The 3DES-EDE Symmetric Encryption Protocol.')
if mibBuilder.loadTexts: usm3DESEDEPrivProtocol.setReference('- Data Encryption Standard, National Institute of Standards and Technology. Federal Information Processing Standard (FIPS) Publication 46-3, (1999, pending approval). Will supersede FIPS Publication 46-2. - Data Encryption Algorithm, American National Standards Institute. ANSI X3.92-1981, (December, 1980). - DES Modes of Operation, National Institute of Standards and Technology. Federal Information Processing Standard (FIPS) Publication 81, (December, 1980). - Data Encryption Algorithm - Modes of Operation, American National Standards Institute. ANSI X3.106-1983, (May 1983). ')
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-3DES-MIB", usm3DESEDEPrivProtocol=usm3DESEDEPrivProtocol, snmpUsmMIB=snmpUsmMIB, PYSNMP_MODULE_ID=snmpUsmMIB)
