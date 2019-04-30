#
# PySNMP MIB module HM2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:18:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Counter64, ObjectIdentity, TimeTicks, iso, enterprises, Counter32, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Counter64", "ObjectIdentity", "TimeTicks", "iso", "enterprises", "Counter32", "MibIdentifier", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2TcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 1))
hm2TcMib.setRevisions(('2011-03-16 00:00',))
if mibBuilder.loadTexts: hm2TcMib.setLastUpdated('201103160000Z')
if mibBuilder.loadTexts: hm2TcMib.setOrganization('Hirschmann Automation and Control GmbH')
hirschmann = MibIdentifier((1, 3, 6, 1, 4, 1, 248))
hm2ConfigurationMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11))
hm2PlatformMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12))
class HmEnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class HmActionValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("noop", 1), ("action", 2))

class HmTimeHHMM24(TextualConvention, OctetString):
    status = 'current'
    displayHint = '5a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 5)

class HmTimeSeconds1970(TextualConvention, Unsigned32):
    status = 'current'

class HmLargeDisplayString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("HM2-TC-MIB", HmTimeHHMM24=HmTimeHHMM24, HmTimeSeconds1970=HmTimeSeconds1970, hirschmann=hirschmann, PYSNMP_MODULE_ID=hm2TcMib, hm2TcMib=hm2TcMib, HmLargeDisplayString=HmLargeDisplayString, hm2ConfigurationMibs=hm2ConfigurationMibs, HmEnabledStatus=HmEnabledStatus, HmActionValue=HmActionValue, hm2PlatformMibs=hm2PlatformMibs)
