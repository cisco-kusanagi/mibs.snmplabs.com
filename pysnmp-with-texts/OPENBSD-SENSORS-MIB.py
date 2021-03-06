#
# PySNMP MIB module OPENBSD-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPENBSD-SENSORS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:35:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, MibIdentifier, Counter32, Unsigned32, TimeTicks, enterprises, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, iso, ModuleIdentity, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Counter32", "Unsigned32", "TimeTicks", "enterprises", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "iso", "ModuleIdentity", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sensorsMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 2))
sensorsMIBObjects.setRevisions(('2012-09-20 00:00', '2012-01-31 00:00', '2008-12-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sensorsMIBObjects.setRevisionsDescriptions(('Add new sensor types.', 'Update email address.', 'Updated for MIB for the OpenBSD snmpd(8) implementation.',))
if mibBuilder.loadTexts: sensorsMIBObjects.setLastUpdated('201209200000Z')
if mibBuilder.loadTexts: sensorsMIBObjects.setOrganization('OpenBSD')
if mibBuilder.loadTexts: sensorsMIBObjects.setContactInfo('Editor: Reyk Floeter EMail: reyk@openbsd.org WWW: http://www.openbsd.org/ Editor: Joel Knight EMail: knight.joel@gmail.com WWW: http://www.packetmischief.ca/openbsd-snmp-mibs/')
if mibBuilder.loadTexts: sensorsMIBObjects.setDescription("The MIB module for gathering information from OpenBSD's kernel sensor framework.")
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 2, 1))
sensorNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorNumber.setStatus('current')
if mibBuilder.loadTexts: sensorNumber.setDescription('The number of sensors present on this system.')
sensorTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2), )
if mibBuilder.loadTexts: sensorTable.setStatus('current')
if mibBuilder.loadTexts: sensorTable.setDescription('A list of individual sensors. The number of entries is given by the value of sensorNumber.')
sensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1), ).setIndexNames((0, "OPENBSD-SENSORS-MIB", "sensorIndex"))
if mibBuilder.loadTexts: sensorEntry.setStatus('current')
if mibBuilder.loadTexts: sensorEntry.setDescription('An entry containing management information applicable to a particular sensor.')
sensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorIndex.setStatus('current')
if mibBuilder.loadTexts: sensorIndex.setDescription('A unique value, greater than zero, for each sensor.')
sensorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDescr.setStatus('current')
if mibBuilder.loadTexts: sensorDescr.setDescription('A description of the sensor indicating what information the sensor is monitoring.')
sensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("temperature", 0), ("fan", 1), ("voltsdc", 2), ("voltsac", 3), ("resistance", 4), ("power", 5), ("current", 6), ("watthour", 7), ("amphour", 8), ("indicator", 9), ("raw", 10), ("percent", 11), ("illuminance", 12), ("drive", 13), ("timedelta", 14), ("humidity", 15), ("freq", 16), ("angle", 17), ("distance", 18), ("pressure", 19), ("accel", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorType.setStatus('current')
if mibBuilder.loadTexts: sensorType.setDescription('Indicates the type of sensor.')
sensorDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDevice.setStatus('current')
if mibBuilder.loadTexts: sensorDevice.setDescription('The name of the sensor driver that provides the sensor.')
sensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorValue.setStatus('current')
if mibBuilder.loadTexts: sensorValue.setDescription('The value the sensor is currently reporting.')
sensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorUnits.setStatus('current')
if mibBuilder.loadTexts: sensorUnits.setDescription('The units that the sensor reports in.')
sensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unspecified", 0), ("ok", 1), ("warn", 2), ("critical", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorStatus.setStatus('current')
if mibBuilder.loadTexts: sensorStatus.setDescription('Indicates whether the sensor value is within an acceptable range.')
mibBuilder.exportSymbols("OPENBSD-SENSORS-MIB", sensorType=sensorType, sensors=sensors, sensorsMIBObjects=sensorsMIBObjects, sensorNumber=sensorNumber, sensorStatus=sensorStatus, sensorIndex=sensorIndex, PYSNMP_MODULE_ID=sensorsMIBObjects, sensorUnits=sensorUnits, sensorEntry=sensorEntry, sensorDevice=sensorDevice, sensorValue=sensorValue, sensorDescr=sensorDescr, sensorTable=sensorTable)
