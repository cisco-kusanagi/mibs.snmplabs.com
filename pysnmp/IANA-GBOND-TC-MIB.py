#
# PySNMP MIB module IANA-GBOND-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-GBOND-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, Counter64, ModuleIdentity, Unsigned32, ObjectIdentity, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Bits, Counter32, mib_2, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Counter64", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Bits", "Counter32", "mib-2", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaGBondTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 215))
ianaGBondTcMIB.setRevisions(('2013-02-20 00:00',))
if mibBuilder.loadTexts: ianaGBondTcMIB.setLastUpdated('201302200000Z')
if mibBuilder.loadTexts: ianaGBondTcMIB.setOrganization('IANA')
class IANAgBondSchemeList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

class IANAgBondScheme(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("g9981", 1), ("g9982", 2), ("g9983", 3))

mibBuilder.exportSymbols("IANA-GBOND-TC-MIB", IANAgBondScheme=IANAgBondScheme, ianaGBondTcMIB=ianaGBondTcMIB, IANAgBondSchemeList=IANAgBondSchemeList, PYSNMP_MODULE_ID=ianaGBondTcMIB)
