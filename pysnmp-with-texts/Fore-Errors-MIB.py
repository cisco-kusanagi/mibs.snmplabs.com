#
# PySNMP MIB module Fore-Errors-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Errors-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
snmpErrors, = mibBuilder.importSymbols("Fore-Common-MIB", "snmpErrors")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, ObjectIdentity, IpAddress, Counter64, Gauge32, iso, ModuleIdentity, Counter32, NotificationType, TimeTicks, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "iso", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
errorLogMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 2, 3))
if mibBuilder.loadTexts: errorLogMib.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: errorLogMib.setOrganization('FORE')
if mibBuilder.loadTexts: errorLogMib.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: errorLogMib.setDescription(' The following two variables are provided as a way of reporting SNMP errors to the management station. The SNMP agent keeps track two variables for each set request (last oid and last error message that was caused by setting the value for last oid). This information is based on the incoming ipaddress and port, so there is only one instance available for each source. The management station will only see errors that is the result of its own set request. If there is no errors available for this source, no value is returned.')
lastLogMessage = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLogMessage.setStatus('current')
if mibBuilder.loadTexts: lastLogMessage.setDescription('The error message that was the result of last set request.')
lastLogMessageOID = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 2, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastLogMessageOID.setStatus('current')
if mibBuilder.loadTexts: lastLogMessageOID.setDescription('The last set request OID that produced an error.')
mibBuilder.exportSymbols("Fore-Errors-MIB", lastLogMessageOID=lastLogMessageOID, lastLogMessage=lastLogMessage, PYSNMP_MODULE_ID=errorLogMib, errorLogMib=errorLogMib)
