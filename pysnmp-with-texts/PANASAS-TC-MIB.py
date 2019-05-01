#
# PySNMP MIB module PANASAS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, IpAddress, Integer32, NotificationType, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, Counter64, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "Counter64", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PanSerialNumber(TextualConvention, OctetString):
    description = 'Serial Number representation'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 32)

class PanBoolean(TextualConvention, Integer32):
    description = 'A boolean value of true(yes) or false(no).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("panFalse", 0), ("panTrue", 1))

class PanTemperature(TextualConvention, Integer32):
    description = 'Temperature in degrees Celcius.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 200)

class PanUtilization(TextualConvention, Integer32):
    description = 'Utilization as a percentage, ie. 15 is 15 percent'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

mibBuilder.exportSymbols("PANASAS-TC-MIB", PanBoolean=PanBoolean, PanSerialNumber=PanSerialNumber, PanTemperature=PanTemperature, PanUtilization=PanUtilization)
