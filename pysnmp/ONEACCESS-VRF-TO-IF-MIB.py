#
# PySNMP MIB module ONEACCESS-VRF-TO-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-VRF-TO-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMIp, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIp")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, IpAddress, iso, Gauge32, Counter32, ObjectIdentity, Unsigned32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "IpAddress", "iso", "Gauge32", "Counter32", "ObjectIdentity", "Unsigned32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacExpIMIPVrfToIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11))
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setLastUpdated('1204051200Z')
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setOrganization('ONE ACCESS')
class OacExpVrfName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

oacExpIMIPVrfToIfTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1), )
if mibBuilder.loadTexts: oacExpIMIPVrfToIfTable.setStatus('current')
oacExpIMIPVrfToIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacExpIMIPVrfToIfEntry.setStatus('current')
oacVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1, 1, 1), OacExpVrfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacVrfName.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-VRF-TO-IF-MIB", PYSNMP_MODULE_ID=oacExpIMIPVrfToIf, oacExpIMIPVrfToIfEntry=oacExpIMIPVrfToIfEntry, oacExpIMIPVrfToIf=oacExpIMIPVrfToIf, OacExpVrfName=OacExpVrfName, oacVrfName=oacVrfName, oacExpIMIPVrfToIfTable=oacExpIMIPVrfToIfTable)
