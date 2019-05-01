#
# PySNMP MIB module EQUALLOGIC-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EQUALLOGIC-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:05:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, Bits, enterprises, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, Counter64, NotificationType, Counter32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "Bits", "enterprises", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter64", "NotificationType", "Counter32", "Unsigned32", "IpAddress")
TextualConvention, TruthValue, RowStatus, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "RowPointer", "DisplayString")
equalLogic = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740))
equalLogic.setRevisions(('2008-05-20 21:09',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: equalLogic.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: equalLogic.setLastUpdated('201403121459Z')
if mibBuilder.loadTexts: equalLogic.setOrganization('EqualLogic Inc.')
if mibBuilder.loadTexts: equalLogic.setContactInfo('Contact: Customer Support Postal: Dell Inc 300 Innovative Way, Suite 301, Nashua, NH 03062 Tel: +1 603-579-9762 E-mail: US-NH-CS-TechnicalSupport@dell.com WEB: www.equallogic.com')
if mibBuilder.loadTexts: equalLogic.setDescription('Equallogic Inc. group information Copyright (c) 2002-2009 by Dell, Inc. All rights reserved. This software may not be copied, disclosed, transferred, or used except in accordance with a license granted by Dell, Inc. This software embodies proprietary information and trade secrets of Dell, Inc. ')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740))
eqlPSSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 12740, 1))
mibBuilder.exportSymbols("EQUALLOGIC-SMI", products=products, eqlPSSeries=eqlPSSeries, PYSNMP_MODULE_ID=equalLogic, equalLogic=equalLogic)
