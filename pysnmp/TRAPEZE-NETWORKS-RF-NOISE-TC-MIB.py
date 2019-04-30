#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-NOISE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-RF-NOISE-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, ModuleIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFNoiseTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 22))
trpzRFNoiseTc.setRevisions(('2011-01-10 00:00',))
if mibBuilder.loadTexts: trpzRFNoiseTc.setLastUpdated('201101100000Z')
if mibBuilder.loadTexts: trpzRFNoiseTc.setOrganization('Trapeze Networks')
class TrpzRFNoiseSourceID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TrpzRFNoiseSourceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 16, 33, 49, 50, 64, 65, 66))
    namedValues = NamedValues(("nsUnknown", 0), ("nsContinuousWave", 1), ("nsVideo", 16), ("nsMicrowaveOven", 33), ("nsPhoneDECT", 49), ("nsPhoneFHSS", 50), ("nsBluetoothAny", 64), ("nsBluetoothHeadset", 65), ("nsBluetoothHandsfree", 66))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-NOISE-TC-MIB", TrpzRFNoiseSourceID=TrpzRFNoiseSourceID, TrpzRFNoiseSourceType=TrpzRFNoiseSourceType, trpzRFNoiseTc=trpzRFNoiseTc, PYSNMP_MODULE_ID=trpzRFNoiseTc)
