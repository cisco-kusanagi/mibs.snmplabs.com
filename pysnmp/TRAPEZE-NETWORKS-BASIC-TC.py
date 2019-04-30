#
# PySNMP MIB module TRAPEZE-NETWORKS-BASIC-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-BASIC-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, IpAddress, Bits, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "IpAddress", "Bits", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzBasicTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 12))
trpzBasicTc.setRevisions(('2008-10-23 00:04',))
if mibBuilder.loadTexts: trpzBasicTc.setLastUpdated('200810230004Z')
if mibBuilder.loadTexts: trpzBasicTc.setOrganization('Trapeze Networks')
class TrpzIpPort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TrpzPhysPortNumber(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class TrpzPhysPortNumberOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1024), )
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-BASIC-TC", TrpzPhysPortNumberOrZero=TrpzPhysPortNumberOrZero, trpzBasicTc=trpzBasicTc, TrpzPhysPortNumber=TrpzPhysPortNumber, TrpzIpPort=TrpzIpPort, PYSNMP_MODULE_ID=trpzBasicTc)
