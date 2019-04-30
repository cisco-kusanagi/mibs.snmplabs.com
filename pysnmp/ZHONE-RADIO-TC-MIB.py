#
# PySNMP MIB module ZHONE-RADIO-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-RADIO-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Counter32, Unsigned32, Bits, NotificationType, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter32", "Unsigned32", "Bits", "NotificationType", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SinglePrecisionFloatingPoint(TextualConvention, Integer32):
    status = 'current'

class SkyZhoneRadioChannelNumber(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'Optimally, the customer should be allowed to use channel numbers \n                or frequencies for channel selection. (A ZMS/NMS preference.) \n                Minimally the user should use channel numbers and be able to see\n                a table of channel to frequency assignments appropriate to\n                the node they are configuring.'

class SkyZhoneOperatingFrequency(TextualConvention, Integer32):
    status = 'current'

class SkyZhoneScientificNotation(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

mibBuilder.exportSymbols("ZHONE-RADIO-TC-MIB", SkyZhoneOperatingFrequency=SkyZhoneOperatingFrequency, SkyZhoneScientificNotation=SkyZhoneScientificNotation, SkyZhoneRadioChannelNumber=SkyZhoneRadioChannelNumber, SinglePrecisionFloatingPoint=SinglePrecisionFloatingPoint)
