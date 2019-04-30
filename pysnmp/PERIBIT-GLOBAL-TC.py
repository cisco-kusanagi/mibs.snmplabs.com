#
# PySNMP MIB module PERIBIT-GLOBAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PERIBIT-GLOBAL-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
pnModules, = mibBuilder.importSymbols("PERIBIT-GLOBAL-REG", "pnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, NotificationType, iso, ModuleIdentity, ObjectIdentity, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Bits, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "NotificationType", "iso", "ModuleIdentity", "ObjectIdentity", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Bits", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pnGlobalTcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 2))
pnGlobalTcModule.setRevisions(('2004-03-15 14:00', '2003-06-26 20:00', '2002-11-07 19:00', '2001-07-29 22:00',))
if mibBuilder.loadTexts: pnGlobalTcModule.setLastUpdated('200107292200Z')
if mibBuilder.loadTexts: pnGlobalTcModule.setOrganization('Peribit Networks, Inc')
class TcAppName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class TcChassisType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("pnOther", 1), ("pnSr50", 2), ("pnSr20", 3), ("pnSr80", 4), ("pnSr100", 5), ("pnSm500", 6), ("pnSr15", 7))

mibBuilder.exportSymbols("PERIBIT-GLOBAL-TC", pnGlobalTcModule=pnGlobalTcModule, PYSNMP_MODULE_ID=pnGlobalTcModule, TcAppName=TcAppName, TcChassisType=TcChassisType)
