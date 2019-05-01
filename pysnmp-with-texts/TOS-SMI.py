#
# PySNMP MIB module TOS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOS-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:24:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, Integer32, Counter64, TimeTicks, Bits, Counter32, Gauge32, Unsigned32, MibIdentifier, iso, ModuleIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Integer32", "Counter64", "TimeTicks", "Bits", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "iso", "ModuleIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
topsec = ModuleIdentity((1, 3, 6, 1, 4, 1, 14331))
topsec.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: topsec.setRevisionsDescriptions(('Initial version.', 'enterprises revised.', 'Mgmt revised.', 'ivtable;some other object changed .', 'system information', 'split the whole mib file into several part', 'edit the file tos-smi.mib',))
if mibBuilder.loadTexts: topsec.setLastUpdated('08-03-14')
if mibBuilder.loadTexts: topsec.setOrganization('TOPSEC')
if mibBuilder.loadTexts: topsec.setContactInfo(' Topsec Beijing China E-mail: support@topsec.com.cn ')
if mibBuilder.loadTexts: topsec.setDescription('The MIB module for management of Topsec Operating System Security Product, independent of the specific encapsulation scheme in use.')
topsecMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5))
topsecExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5, 4))
objects = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5, 5))
tosMib = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1))
mibBuilder.exportSymbols("TOS-SMI", topsec=topsec, PYSNMP_MODULE_ID=topsec, topsecMgmt=topsecMgmt, topsecExperiment=topsecExperiment, objects=objects, tosMib=tosMib)
