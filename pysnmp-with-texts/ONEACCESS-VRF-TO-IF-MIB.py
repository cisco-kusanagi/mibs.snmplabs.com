#
# PySNMP MIB module ONEACCESS-VRF-TO-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-VRF-TO-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacExpIMIp, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, Integer32, Gauge32, iso, Counter64, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "Integer32", "Gauge32", "iso", "Counter64", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacExpIMIPVrfToIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11))
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setLastUpdated('1204051200Z')
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setOrganization('ONE ACCESS')
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Général de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 54 Fax: (+33) 01 41 87 74 39 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacExpIMIPVrfToIf.setDescription('This MIB module lists all the interfaces attached to a configured VRF.')
class OacExpVrfName(TextualConvention, OctetString):
    description = 'Textual convention for vrf name.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

oacExpIMIPVrfToIfTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1), )
if mibBuilder.loadTexts: oacExpIMIPVrfToIfTable.setStatus('current')
if mibBuilder.loadTexts: oacExpIMIPVrfToIfTable.setDescription('Table of correspondance between VRF and interfaces')
oacExpIMIPVrfToIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacExpIMIPVrfToIfEntry.setStatus('current')
if mibBuilder.loadTexts: oacExpIMIPVrfToIfEntry.setDescription('Each entry corresponds to a an interface and the VRF it belongs to')
oacVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 11, 1, 1, 1), OacExpVrfName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacVrfName.setStatus('current')
if mibBuilder.loadTexts: oacVrfName.setDescription('The name of the VRF the interface belong to')
mibBuilder.exportSymbols("ONEACCESS-VRF-TO-IF-MIB", oacExpIMIPVrfToIf=oacExpIMIPVrfToIf, oacVrfName=oacVrfName, OacExpVrfName=OacExpVrfName, PYSNMP_MODULE_ID=oacExpIMIPVrfToIf, oacExpIMIPVrfToIfTable=oacExpIMIPVrfToIfTable, oacExpIMIPVrfToIfEntry=oacExpIMIPVrfToIfEntry)
