#
# PySNMP MIB module NTWS-BASIC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-BASIC-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, MibIdentifier, ObjectIdentity, Counter64, TimeTicks, Gauge32, Unsigned32, Bits, iso, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "TimeTicks", "Gauge32", "Unsigned32", "Bits", "iso", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsBasicTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 12))
ntwsBasicTc.setRevisions(('2008-10-23 00:04',))
if mibBuilder.loadTexts: ntwsBasicTc.setLastUpdated('200810230004Z')
if mibBuilder.loadTexts: ntwsBasicTc.setOrganization('Nortel Networks')
class NtwsIpPort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class NtwsPhysPortNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class NtwsPhysPortNumberOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1024), )
mibBuilder.exportSymbols("NTWS-BASIC-TC", PYSNMP_MODULE_ID=ntwsBasicTc, NtwsPhysPortNumber=NtwsPhysPortNumber, NtwsPhysPortNumberOrZero=NtwsPhysPortNumberOrZero, NtwsIpPort=NtwsIpPort, ntwsBasicTc=ntwsBasicTc)
