#
# PySNMP MIB module DSX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DSX-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:54:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ntEnterpriseDataTasmanInterfaces, ntEnterpriseDataTasmanMgmt, ntEnterpriseDataTasmanModules = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanInterfaces", "ntEnterpriseDataTasmanMgmt", "ntEnterpriseDataTasmanModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, Integer32, ObjectIdentity, Unsigned32, Counter64, TimeTicks, iso, Gauge32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "TimeTicks", "iso", "Gauge32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nndsxTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 3, 2))
nndsxTC.setRevisions(('1999-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nndsxTC.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: nndsxTC.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: nndsxTC.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nndsxTC.setContactInfo(' Nortel Networks 8200 Dixie Road Brampton, Ontario L6T 5P6 Canada 1-800-4Nortel www.nortelnetworks.com ')
if mibBuilder.loadTexts: nndsxTC.setDescription(' Interface MIB definitions for T1/E1 interface modules.')
class AlarmStatus(TextualConvention, Integer32):
    description = 'This data type is used to represent the status of an alarm.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("off", 0), ("on", 1))

class LEDState(TextualConvention, Integer32):
    description = 'Different states LED can be in.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("led-off", 1), ("led-green", 2), ("led-red", 3), ("led-yellow", 4), ("led-blinking-green", 5), ("led-blinking-red", 6), ("led-blinking-yellow", 7))

nndsxMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1))
nndsxT1E1IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2))
nndsxT3E3IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 3))
mibBuilder.exportSymbols("DSX-TC-MIB", AlarmStatus=AlarmStatus, PYSNMP_MODULE_ID=nndsxTC, nndsxTC=nndsxTC, nndsxT3E3IfGroup=nndsxT3E3IfGroup, LEDState=LEDState, nndsxT1E1IfGroup=nndsxT1E1IfGroup, nndsxMIB=nndsxMIB)
