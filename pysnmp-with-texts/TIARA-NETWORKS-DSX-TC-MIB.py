#
# PySNMP MIB module TIARA-NETWORKS-DSX-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-DSX-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Bits, Unsigned32, ModuleIdentity, Counter64, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Unsigned32", "ModuleIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraInterfaces, tiaraMgmt, tiaraModules = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraInterfaces", "tiaraMgmt", "tiaraModules")
dsxTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 3, 2))
dsxTC.setRevisions(('1999-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dsxTC.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: dsxTC.setLastUpdated('9904230000Z')
if mibBuilder.loadTexts: dsxTC.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: dsxTC.setContactInfo(' Tiara Networks Customer Service Postal: 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: dsxTC.setDescription(' Interface MIB definitions for Tiara T1/E1 interface modules.')
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

dsxMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 1))
dsxT1E1IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 2))
dsxT3E3IfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3174, 2, 7, 1, 3))
mibBuilder.exportSymbols("TIARA-NETWORKS-DSX-TC-MIB", dsxTC=dsxTC, LEDState=LEDState, dsxT3E3IfGroup=dsxT3E3IfGroup, dsxT1E1IfGroup=dsxT1E1IfGroup, AlarmStatus=AlarmStatus, PYSNMP_MODULE_ID=dsxTC, dsxMIB=dsxMIB)
